#!/usr/bin/env python3
"""
Example script to demonstrate how to extract lemma from noun_to_define_final.xlsx
"""

import pandas as pd
import sys

def get_lemma_at_row(file_path, row_number):
    """
    Extract the lemma value from a specific row in the Excel file.
    
    Args:
        file_path: Path to the Excel file
        row_number: Row number to extract (1-indexed as used in the script)
    
    Returns:
        The lemma value at the specified row
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Convert 1-indexed row to 0-indexed for pandas
        row_index = row_number - 1
        
        # Check if row exists
        if row_index < 0 or row_index >= len(df):
            return f"Error: Row {row_number} does not exist. File has {len(df)} rows."
        
        # Check if 'lemma' column exists (lowercase)
        if 'lemma' not in df.columns:
            return f"Error: 'lemma' column not found. Available columns: {list(df.columns)}"
        
        # Get the lemma value
        lemma = df.loc[row_index, 'lemma']
        
        return lemma
        
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"Error reading Excel file: {e}"

def main():
    """Main function to demonstrate lemma extraction"""
    
    # File path
    excel_file = "noun_to_define_final.xlsx"
    
    # Read current count from count.txt
    try:
        with open("count.txt", "r") as f:
            current_row = int(f.read().strip())
    except:
        current_row = 1
    
    # Get lemma at current row
    lemma = get_lemma_at_row(excel_file, current_row)
    
    print(f"Row {current_row}: Lemma = '{lemma}'")
    
    # Example: Get lemmas for rows 1-5
    print("\nExample - First 5 lemmas:")
    for row in range(1, 6):
        lemma = get_lemma_at_row(excel_file, row)
        print(f"Row {row}: {lemma}")

if __name__ == "__main__":
    main()