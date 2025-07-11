import pandas as pd

# Read the Excel file
df = pd.read_excel('noun_to_define_final.xlsx')

# Get the lemma at row 2 (index 1 in pandas)
lemma = df.loc[1, 'lemma']
wiki_frequency = df.loc[1, 'wiki_frequency']

print(f"Lemma at row 2: {lemma}")
print(f"Wiki frequency: {wiki_frequency}")

# Calculate pos_frequency if total wiki frequency is known
# For now, just print the raw frequency
print(f"\nFull row 2 data:")
print(df.loc[1])