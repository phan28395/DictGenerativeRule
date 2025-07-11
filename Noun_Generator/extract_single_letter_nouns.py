#!/usr/bin/env python3
"""
Script to extract single-letter nouns from wordFrequency.xlsx
and generate output files with extracted data and statistics.
"""

import pandas as pd
import sys
from pathlib import Path

def extract_single_letter_nouns(input_file='wordFrequency.xlsx', output_file='single_word_nouns.xlsx', stats_file='noun_statistics.txt'):
    """
    Extract single-word nouns (without spaces) from the '1 lemmas' tab of an Excel file.
    
    Args:
        input_file: Path to input Excel file
        output_file: Path to output Excel file
        stats_file: Path to statistics text file
    """
    try:
        # Read the '1 lemmas' tab from the Excel file
        df = pd.read_excel(input_file, sheet_name='1 lemmas')
        print(f"Successfully loaded '{input_file}' with {len(df)} rows")
        
        # Filter for single-word nouns (no spaces) with PoS = 'n'
        single_word_nouns = df[(~df['lemma'].str.contains(' ', na=False)) & (df['PoS'] == 'n')].copy()
        print(f"Found {len(single_word_nouns)} single-word nouns")
        
        # Create output dataframe with required columns
        output_df = pd.DataFrame({
            'id': range(1, len(single_word_nouns) + 1),
            'lemma': single_word_nouns['lemma'].values,
            'PoS': 'n',
            'PROPER_NOUN': ''  # Empty column as requested
        })
        
        # Save to Excel
        output_df.to_excel(output_file, index=False)
        print(f"Saved {len(output_df)} single-word nouns to '{output_file}'")
        
        # Generate statistics for multi-word nouns (containing spaces)
        multi_word_nouns = df[(df['lemma'].str.contains(' ', na=False)) & (df['PoS'] == 'n')]
        
        # Create statistics
        stats = []
        stats.append("=== Noun Statistics ===")
        stats.append(f"Total nouns in dataset: {len(df[df['PoS'] == 'n'])}")
        stats.append(f"Single-word nouns (extracted): {len(single_word_nouns)}")
        stats.append(f"Multi-word nouns (containing spaces): {len(multi_word_nouns)}")
        stats.append("")
        stats.append("=== Multi-word Noun Examples (first 20) ===")
        
        # Show examples of multi-word nouns
        if len(multi_word_nouns) > 0:
            for i, lemma in enumerate(multi_word_nouns['lemma'].head(20)):
                stats.append(f"{i+1}. {lemma}")
        
        # Write statistics to file
        with open(stats_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(stats))
        
        print(f"Statistics saved to '{stats_file}'")
        
        # Print summary
        print("\nSummary:")
        print('\n'.join(stats))
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found!")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Required column not found - {e}")
        print("Please ensure the Excel file has '1 lemmas' sheet with 'lemma' and 'PoS' columns")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Run the extraction
    extract_single_letter_nouns()