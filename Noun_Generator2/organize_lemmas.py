#!/usr/bin/env python3
"""
Script to organize lemmas from Excel file into JSON files with folder structure.
Extracts lemmas from noun_to_define_final.xlsx and creates JSON files following JSON-Schema.json structure.
"""

import pandas as pd
import json
import os
from pathlib import Path

def create_lemma_json_structure(lemma):
    """Create a JSON structure for a lemma according to the schema."""
    return {
        "word": lemma,
        "pos": "noun",
        "inflections": {
            "plural": "",
            "possessive": ""
        },
        "pos_frequency": 0.0,
        "meanings": []
    }

def organize_lemmas():
    """Main function to organize lemmas into folders and JSON files."""
    # Read the Excel file
    df = pd.read_excel('noun_to_define_final.xlsx')
    
    # Extract lemmas (first 2000 as requested)
    lemmas = df['lemma'].tolist()[:2000]
    
    # Create main directory
    base_dir = Path('lemmas_to_define')
    base_dir.mkdir(exist_ok=True)
    
    # Process lemmas in chunks
    lemmas_per_main_folder = 500  # 4 folders × 500 = 2000
    lemmas_per_json = 50          # 50 lemmas per JSON file
    json_files_per_subfolder = 10  # 500 / 50 = 10 JSON files per subfolder
    
    lemma_index = 0
    
    # Create 4 main folders (0-499, 500-999, 1000-1499, 1500-1999)
    for main_folder_idx in range(4):
        start_idx = main_folder_idx * lemmas_per_main_folder + 1
        end_idx = (main_folder_idx + 1) * lemmas_per_main_folder
        
        main_folder_name = f"{start_idx} to {end_idx}"
        main_folder_path = base_dir / main_folder_name
        main_folder_path.mkdir(exist_ok=True)
        
        # Create JSON files in this main folder
        for json_idx in range(json_files_per_subfolder):
            # Collect 50 lemmas for this JSON file
            json_data = []
            
            for _ in range(lemmas_per_json):
                if lemma_index < len(lemmas):
                    lemma = lemmas[lemma_index]
                    json_data.append(create_lemma_json_structure(lemma))
                    lemma_index += 1
            
            # Write JSON file
            if json_data:
                json_start = json_idx * lemmas_per_json + start_idx
                json_end = json_start + len(json_data) - 1
                json_filename = f"lemmas_{json_start}_to_{json_end}.json"
                json_path = main_folder_path / json_filename
                
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, indent=2, ensure_ascii=False)
                
                print(f"Created: {json_path}")
    
    print(f"\nTotal lemmas processed: {lemma_index}")
    print(f"Files created in: {base_dir}")

if __name__ == "__main__":
    organize_lemmas()