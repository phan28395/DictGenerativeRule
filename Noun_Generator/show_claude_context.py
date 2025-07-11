#!/usr/bin/env python3
"""
This script demonstrates what information Claude would access when processing
the prompt about generating entries for specific lemmas.
"""

import pandas as pd
import json
import sys

def show_context_for_row(row_number):
    """Show what Claude would see when processing a specific row"""
    
    print(f"\n=== Context for Row {row_number} ===\n")
    
    # 1. Get lemma from Excel file
    try:
        df = pd.read_excel("noun_to_define_final.xlsx")
        row_index = row_number - 1
        
        if row_index < 0 or row_index >= len(df):
            print(f"Error: Row {row_number} does not exist")
            return
            
        lemma = df.loc[row_index, 'lemma']
        pos = df.loc[row_index, 'PoS'] if 'PoS' in df.columns else 'N/A'
        frequency = df.loc[row_index, 'wiki_frequency'] if 'wiki_frequency' in df.columns else 'N/A'
        
        print(f"1. Excel Data (noun_to_define_final.xlsx):")
        print(f"   - Row: {row_number}")
        print(f"   - Lemma: {lemma}")
        print(f"   - PoS: {pos}")
        print(f"   - Wiki Frequency: {frequency}")
        
    except Exception as e:
        print(f"Error reading Excel: {e}")
        return
    
    # 2. Show JSON Schema structure
    print("\n2. JSON Schema (JSON-Schema.json):")
    try:
        with open("JSON-Schema.json", "r") as f:
            schema = json.load(f)
            print("   Schema defines the structure for noun entries")
            # Just show the top-level structure
            if "properties" in schema:
                print(f"   Properties: {list(schema['properties'].keys())}")
    except Exception as e:
        print(f"   Error reading schema: {e}")
    
    # 3. Show Noun Rules
    print("\n3. Noun Rules (Noun_Rule_Final.md):")
    try:
        with open("Noun_Rule_Final.md", "r") as f:
            lines = f.readlines()[:10]  # Show first 10 lines
            print("   " + "   ".join(lines[:3]))
            print("   [... full rules document ...]")
    except Exception as e:
        print(f"   Error reading rules: {e}")
    
    # 4. Show current entries count
    print("\n4. Current Noun Entries (Noun-Entries.json):")
    try:
        with open("Noun-Entries.json", "r") as f:
            entries = json.load(f)
            if isinstance(entries, list):
                print(f"   Current entries count: {len(entries)}")
                if entries:
                    print(f"   Last entry lemma: {entries[-1].get('lemma', 'N/A')}")
            else:
                print("   Entries format not recognized")
    except Exception as e:
        print(f"   Error reading entries: {e}")
    
    print(f"\n5. Claude's Task:")
    print(f"   Generate a dictionary entry for the lemma '{lemma}' following the")
    print(f"   structure in JSON-Schema.json and rules in Noun_Rule_Final.md,")
    print(f"   then add it to Noun-Entries.json")
    print("\n" + "="*50)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            row = int(sys.argv[1])
            show_context_for_row(row)
        except ValueError:
            print("Please provide a valid row number")
    else:
        # Show context for rows 1-3 as examples
        for row in range(1, 4):
            show_context_for_row(row)