#!/usr/bin/env python3
"""
Script to extract non-proper nouns (PROPER_NOUN = 'NO') from Excel file
and save to a new Excel file with id, lemma, and PoS columns.
"""

import pandas as pd
import sys

def extract_non_proper_nouns(input_file='PropNoun&Noun_single_word_nouns.xlsx', output_file='noun_to_define.xlsx'):
    """
    Extract lemmas where PROPER_NOUN = 'NO' and save to new Excel file.
    
    Args:
        input_file: Path to input Excel file
        output_file: Path to output Excel file
    """
    try:
        # Read the Excel file
        df = pd.read_excel(input_file)
        print(f"Successfully loaded '{input_file}' with {len(df)} rows")
        
        # Filter for rows where PROPER_NOUN = 'NO'
        non_proper_nouns = df[df['PROPER_NOUN'] == 'NO'].copy()
        print(f"Found {len(non_proper_nouns)} non-proper nouns")
        
        # Create output dataframe with required columns
        output_df = pd.DataFrame({
            'id': range(1, len(non_proper_nouns) + 1),
            'lemma': non_proper_nouns['lemma'].values,
            'PoS': 'n'  # All should be 'n' as requested
        })
        
        # Save to Excel
        output_df.to_excel(output_file, index=False)
        print(f"Saved {len(output_df)} non-proper nouns to '{output_file}'")
        
        # Print first few examples
        print("\nFirst 10 entries:")
        print(output_df.head(10).to_string(index=False))
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found!")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Required column not found - {e}")
        print("Please ensure the Excel file has 'lemma' and 'PROPER_NOUN' columns")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Run the extraction
    extract_non_proper_nouns()