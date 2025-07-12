import pandas as pd
import os

# Read the Excel file
excel_file = 'wordFrequency.xlsx'
df = pd.read_excel(excel_file, sheet_name='1 lemmas')

# Filter for nouns (where column C = 'n')
# Column B is lemma, Column C is PoS
nouns_df = df[df.iloc[:, 2] == 'n'].copy()

# Create output with id and lemma columns
output_df = pd.DataFrame()
output_df['id'] = range(1, len(nouns_df) + 1)
output_df['lemma'] = nouns_df.iloc[:, 1].values

# Save to text file
output_file = 'noun_list.txt'
os.makedirs('Noun_Generator', exist_ok=True)
output_df.to_csv(output_file, sep='\t', index=False)

print(f"Extracted {len(output_df)} nouns to {output_file}")