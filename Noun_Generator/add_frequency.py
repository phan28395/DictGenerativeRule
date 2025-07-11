#!/usr/bin/env python3
"""
Add Wikipedia frequency data to XLSX file.
Flexible script that allows specifying input file, sheet, and column names.
"""

import pandas as pd
import requests
import os
import sys
import argparse
from pathlib import Path


class WikipediaFrequencyAdder:
    def __init__(self):
        self.frequency_data = {}
        self.cache_dir = Path.home() / '.cache' / 'wikipedia_frequency'
        self.cache_file = self.cache_dir / 'wikipedia_frequencies.txt'
        
    def download_frequency_data(self):
        """Download Wikipedia frequency data if not cached."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        if self.cache_file.exists():
            print(f"Using cached frequency data from {self.cache_file}")
            return str(self.cache_file)
        
        print("Downloading Wikipedia frequency data (this only happens once)...")
        url = "https://raw.githubusercontent.com/IlyaSemenov/wikipedia-word-frequency/master/results/enwiki-2023-04-13.txt"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            print(f"✓ Downloaded and cached frequency data to {self.cache_file}")
            return str(self.cache_file)
            
        except requests.RequestException as e:
            print(f"Error downloading frequency data: {e}")
            sys.exit(1)
    
    def load_frequency_data(self):
        """Load frequency data into memory."""
        filepath = self.download_frequency_data()
        
        print("Loading frequency data...")
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split()
                    if len(parts) >= 2:
                        word = parts[0].lower()
                        try:
                            frequency = int(parts[1])
                            self.frequency_data[word] = frequency
                        except ValueError:
                            continue
        
        print(f"✓ Loaded {len(self.frequency_data):,} words with frequencies")
    
    def get_frequency(self, word):
        """Get raw frequency for a word."""
        if pd.isna(word):
            return 0
        word = str(word).lower().strip()
        return self.frequency_data.get(word, 0)
    
    def process_file(self, input_file, sheet_name, word_column, freq_column):
        """Process the XLSX file and add frequency data."""
        # Read the Excel file
        print(f"\nReading '{input_file}', sheet '{sheet_name}'...")
        try:
            df = pd.read_excel(input_file, sheet_name=sheet_name)
            print(f"✓ Loaded {len(df):,} rows")
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
        
        # Check if word column exists
        if word_column not in df.columns:
            print(f"Error: Column '{word_column}' not found in sheet '{sheet_name}'")
            print(f"Available columns: {list(df.columns)}")
            sys.exit(1)
        
        # Add frequency data
        print(f"\nAdding frequency data to column '{freq_column}'...")
        frequencies = []
        
        for i, word in enumerate(df[word_column]):
            if i % 1000 == 0:
                print(f"  Processing {i:,} / {len(df):,} words...", end='\r')
            
            freq = self.get_frequency(word)
            frequencies.append(freq)
        
        df[freq_column] = frequencies
        print(f"\n✓ Added frequency data for all {len(df):,} words")
        
        # Save the file
        output_file = input_file.replace('.xlsx', '_with_frequency.xlsx')
        df.to_excel(output_file, sheet_name=sheet_name, index=False)
        print(f"\n✓ Saved to: {output_file}")
        
        # Show statistics
        print("\n=== Frequency Statistics ===")
        print(f"Words found in Wikipedia: {len([f for f in frequencies if f > 0]):,}")
        print(f"Words not found (frequency = 0): {len([f for f in frequencies if f == 0]):,}")
        print(f"Average frequency (excluding zeros): {sum(frequencies) / len([f for f in frequencies if f > 0]):,.0f}")
        print(f"Maximum frequency: {max(frequencies):,}")
        
        # Show examples
        print("\n=== Sample Results ===")
        sample_df = df[[word_column, freq_column]].head(10)
        for _, row in sample_df.iterrows():
            print(f"{row[word_column]:30} | Frequency: {row[freq_column]:,}")


def main():
    parser = argparse.ArgumentParser(description='Add Wikipedia frequency data to XLSX file')
    parser.add_argument('--file', type=str, help='Input XLSX file path')
    parser.add_argument('--sheet', type=str, help='Sheet/tab name')
    parser.add_argument('--word-column', type=str, help='Column containing words/lemmas')
    parser.add_argument('--freq-column', type=str, help='Column name for frequency output')
    
    args = parser.parse_args()
    
    # Interactive mode if arguments not provided
    if not args.file:
        print("=== Wikipedia Frequency Adder ===\n")
        args.file = input("Enter XLSX file path: ").strip()
    
    if not args.sheet:
        args.sheet = input("Enter sheet/tab name: ").strip()
    
    if not args.word_column:
        args.word_column = input("Enter column name containing words/lemmas: ").strip()
    
    if not args.freq_column:
        args.freq_column = input("Enter column name for frequency output: ").strip()
    
    # Process the file
    adder = WikipediaFrequencyAdder()
    adder.load_frequency_data()
    adder.process_file(args.file, args.sheet, args.word_column, args.freq_column)


if __name__ == "__main__":
    main()