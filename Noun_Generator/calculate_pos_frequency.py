import pandas as pd

# Read the Excel file
df = pd.read_excel('noun_to_define_final.xlsx')

# Get the data for "are" (row 2)
lemma = df.loc[1, 'lemma']
wiki_frequency = df.loc[1, 'wiki_frequency']

print(f"Lemma: {lemma}")
print(f"Wiki frequency as noun: {wiki_frequency}")

# Since we don't have total frequency data, we'll need to estimate
# For common words like "are", the noun usage is typically very low
# "are" is primarily used as a verb (to be), so noun usage would be minimal
# Based on linguistic patterns, we can estimate:
pos_frequency = 0.001  # 0.1% - very low noun usage for "are"

print(f"Estimated pos_frequency: {pos_frequency}")