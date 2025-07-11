#!/bin/bash

# Change to the correct directory
cd /home/phanvu/Documents/Company/DictionaryContentGenerator/Noun_Generator

# Read current count from count.txt, default to 1 if file doesn't exist or is empty
if [ -f "count.txt" ] && [ -s "count.txt" ]; then
    x=$(cat count.txt | tr -d '[:space:]')
    # Validate that x is a number
    if ! [[ "$x" =~ ^[0-9]+$ ]]; then
        x=1
    fi
else
    x=1
fi

# Check if we've already generated 20 entries
if [ "$x" -gt 20 ]; then
    echo "Already generated 20 entries. Stopping."
    exit 0
fi

echo "Processing row $x..."
echo "Running Claude (this may take a minute)..."

# Run claude command with the complex prompt
claude -p "Base on the file Noun_Rule_Final.md, generate entry with the structure outlined in JSON-Schema.json and add to the JSON-File Noun-Entries.json for the Lemma in column \"Lemma\" at the row $x in the file noun_to_define_final.xlsx, then add 1 to $x in count.txt. If 20 entries is generated then stop"

# Check if claude command succeeded
if [ $? -eq 0 ]; then
    echo "Claude completed successfully"
    # Increment counter and save to count.txt
    ((x++))
    echo "$x" > count.txt
else
    echo "Claude command failed. Keeping count at $x"
fi

echo "Processed entry. Current count: $x"

# Check if we've reached 20 entries
if [ "$x" -gt 20 ]; then
    echo "Reached 20 entries. Process complete."
fi