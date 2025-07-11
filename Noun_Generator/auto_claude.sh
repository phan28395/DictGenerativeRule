#!/bin/bash

# Change to the correct directory
cd /home/phanvu/Documents/Company/DictionaryContentGenerator/Noun_Generator

# Read current count from count.txt, default to 1 if file doesn't exist or is empty
if [ -f "count.txt" ] && [ -s "count.txt" ]; then
    x=$(tail -n 1 count.txt | tr -d '[:space:]')
    # Validate that x is a number
    if ! [[ "$x" =~ ^[0-9]+$ ]]; then
        x=1
    fi
    # If x is 0, start from 1
    if [ "$x" -eq 0 ]; then
        x=1
    fi
else
    x=1
fi

# Calculate the end of this batch (process 20 items)
start_x=$x
end_x=$((x + 19))

echo "Starting batch from row $start_x to row $end_x"
echo "$(date '+%Y-%m-%d %H:%M:%S') - Starting batch: rows $start_x to $end_x" >> track_progress.txt

# Collect all 20 lemmas first
echo "Collecting lemmas for batch processing..."
lemmas_list=""
rows_list=""
actual_end=$start_x

# Get all lemmas for this batch
for row in $(seq $start_x $end_x); do
    lemma=$(python3 -c "
import pandas as pd
try:
    df = pd.read_excel('noun_to_define_final.xlsx')
    row_idx = $row - 1  # Convert to 0-based index
    if row_idx < len(df):
        print(df.iloc[row_idx]['lemma'])
    else:
        print('ROW_NOT_FOUND')
except Exception as e:
    print(f'ERROR: {e}')
")
    
    if [ "$lemma" = "ROW_NOT_FOUND" ]; then
        echo "No more rows to process. Stopping at row $row"
        break
    fi
    
    if [[ "$lemma" == ERROR:* ]]; then
        echo "Error getting lemma for row $row: $lemma"
        exit 1
    fi
    
    # Add to lists
    if [ -z "$lemmas_list" ]; then
        lemmas_list="$lemma"
        rows_list="$row"
    else
        lemmas_list="$lemmas_list, $lemma"
        rows_list="$rows_list, $row"
    fi
    actual_end=$row
    echo "Collected: $lemma (row $row)"
done

echo "Collected $(($actual_end - $start_x + 1)) lemmas"
echo "Running Claude with batch of lemmas..."

# Run claude command with all lemmas at once
claude --dangerously-skip-permissions --verbose -p "Base on the file Noun_Rule_Final.md, generate entries with the structure outlined in JSON-Schema.json and add to the JSON-File Noun-Entries.json for the following Lemmas from noun_to_define_final.xlsx:

Rows: $rows_list
Lemmas: $lemmas_list

Process all these lemmas and add them to the JSON file. IMPORTANT: If any word has pos_frequency less than 0.021 (2.1%), still include the lemma and pos_frequency fields but skip generating entries for all other features - just leave them empty or minimal."

# Check if claude command succeeded
if [ $? -eq 0 ]; then
    echo "Claude completed successfully"
    # Log all processed lemmas
    for row in $(seq $start_x $actual_end); do
        lemma=$(python3 -c "
import pandas as pd
df = pd.read_excel('noun_to_define_final.xlsx')
print(df.iloc[$row - 1]['lemma'])
")
        echo "$(date '+%Y-%m-%d %H:%M:%S') - lemma $lemma processed (row $row)" >> track_progress.txt
    done
    # Save next position to count.txt
    echo "$((actual_end + 1))" > count.txt
else
    echo "Claude command failed. Keeping count at $start_x"
    # Log failure to track_progress.txt
    echo "$(date '+%Y-%m-%d %H:%M:%S') - FAILED: batch starting at row $start_x" >> track_progress.txt
    # Save current position so next run can retry this batch
    echo "$start_x" > count.txt
    exit 1
fi

echo "Batch complete. Processed rows $start_x to $actual_end"
echo "Next batch will start from row $((actual_end + 1))"