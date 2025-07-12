import csv
import os

# Read the noun list
with open('noun_list.txt', 'r') as f:
    lines = f.readlines()[1:]  # Skip header
    
nouns = []
for line in lines:
    parts = line.strip().split('\t')
    if len(parts) >= 2:
        noun_id, lemma = parts[0], parts[1]
        nouns.append({'id': noun_id, 'lemma': lemma})

# Define CSV headers based on CLAUDE.md requirements
headers = [
    'id', 'lemma', 'inflections', 'pos_frequency', 'meanings', 
    'definition', 'domain', 'register', 'collocations', 'emoji',
    'countability', 'semantic_category', 'synonyms', 'examples', 
    'frequency_meaning'
]

# Create CSV files
for i in range(0, len(nouns), 500):
    # Determine folder
    folder_start = i + 1
    folder_end = min(i + 500, len(nouns))
    folder_name = f"Nouns/lemmas_{folder_start}_to_{folder_end}"
    
    # Create folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)
    
    # Create CSV files in this folder (50 nouns per file)
    for j in range(i, min(i + 500, len(nouns)), 50):
        file_start = j + 1
        file_end = min(j + 50, len(nouns))
        filename = f"{folder_name}/lemmas_{file_start}_to_{file_end}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            
            # Write rows for each noun in this batch
            for k in range(j, min(j + 50, len(nouns))):
                noun = nouns[k]
                row = {
                    'id': noun['id'],
                    'lemma': noun['lemma'],
                    'inflections': '',
                    'pos_frequency': '',
                    'meanings': '',
                    'definition': '',
                    'domain': '',
                    'register': '',
                    'collocations': '',
                    'emoji': '',
                    'countability': '',
                    'semantic_category': '',
                    'synonyms': '',
                    'examples': '',
                    'frequency_meaning': ''
                }
                writer.writerow(row)
        
        print(f"Created {filename}")

print("All CSV files created successfully!")