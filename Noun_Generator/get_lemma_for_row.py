#!/usr/bin/env python3
"""
Script to extract lemma for a specific row from noun_to_define_final.xlsx
Usage: python3 get_lemma_for_row.py <row_number>
"""

import pandas as pd
import sys

def get_lemma_at_row(row_number):
    """Extract the lemma value from a specific row in noun_to_define_final.xlsx"""
    try:
        # Read the Excel file
        df = pd.read_excel("noun_to_define_final.xlsx")
        
        # Convert 1-indexed row to 0-indexed for pandas
        row_index = row_number - 1
        
        # Check if row exists
        if row_index < 0 or row_index >= len(df):
            return None
        
        # Get the lemma value
        lemma = df.loc[row_index, 'lemma']
        
        return lemma
        
    except Exception:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_lemma_for_row.py <row_number>")
        sys.exit(1)
    
    try:
        row_number = int(sys.argv[1])
        lemma = get_lemma_at_row(row_number)
        
        if lemma:
            print(lemma)
        else:
            print(f"Error: Could not get lemma for row {row_number}")
            sys.exit(1)
            
    except ValueError:
        print("Error: Row number must be an integer")
        sys.exit(1)