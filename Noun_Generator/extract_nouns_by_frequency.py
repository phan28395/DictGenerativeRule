#!/usr/bin/env python3
import pandas as pd
import argparse
import sys

def extract_nouns(input_file, output_file, column_name, operator, value):
    """
    Extract nouns based on frequency constraints and save to new Excel file
    
    Args:
        input_file: Path to the input xlsx file
        output_file: Path to the output xlsx file
        column_name: Column to filter (e.g., 'wiki_frequency')
        operator: Comparison operator ('>', '<', '>=', '<=', '==')
        value: Threshold value
    """
    try:
        # Read the Excel file
        print(f"Reading {input_file}...")
        df = pd.read_excel(input_file)
        print(f"Total rows: {len(df):,}")
        
        # Check if the column exists
        if column_name not in df.columns:
            print(f"Error: Column '{column_name}' not found in the Excel file.")
            print(f"Available columns: {', '.join(df.columns)}")
            return
        
        # Convert value to appropriate type
        try:
            value = float(value)
        except ValueError:
            print(f"Error: Value '{value}' must be a number.")
            return
        
        # Apply the filter based on operator
        print(f"\nApplying filter: {column_name} {operator} {value}")
        if operator == '>':
            filtered_df = df[df[column_name] > value]
        elif operator == '<':
            filtered_df = df[df[column_name] < value]
        elif operator == '>=':
            filtered_df = df[df[column_name] >= value]
        elif operator == '<=':
            filtered_df = df[df[column_name] <= value]
        elif operator == '==':
            filtered_df = df[df[column_name] == value]
        else:
            print(f"Error: Invalid operator '{operator}'. Use one of: >, <, >=, <=, ==")
            return
        
        # Sort by frequency in descending order
        filtered_df = filtered_df.sort_values(by=column_name, ascending=False)
        
        # Save to new Excel file
        filtered_df.to_excel(output_file, index=False)
        print(f"\n✓ Extracted {len(filtered_df):,} rows")
        print(f"✓ Saved to: {output_file}")
        
        # Show statistics
        if 'lemma' in filtered_df.columns:
            unique_lemmas = filtered_df['lemma'].nunique()
            print(f"\nStatistics:")
            print(f"- Unique lemmas: {unique_lemmas:,}")
            print(f"- Total entries: {len(filtered_df):,}")
            print(f"- Min {column_name}: {filtered_df[column_name].min():,.0f}")
            print(f"- Max {column_name}: {filtered_df[column_name].max():,.0f}")
            print(f"- Mean {column_name}: {filtered_df[column_name].mean():,.0f}")
            
            # Show top 5 entries
            print(f"\nTop 5 entries by {column_name}:")
            top_5 = filtered_df.head(5)
            for i, (_, row) in enumerate(top_5.iterrows(), 1):
                print(f"  {i}. {row['lemma']:<20} | {column_name}: {row[column_name]:,.0f}")
                
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description='Extract nouns based on frequency constraints to new Excel file',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python extract_nouns_by_frequency.py --greater-equal 1000
  python extract_nouns_by_frequency.py --less 500 --output custom_output.xlsx
  python extract_nouns_by_frequency.py --greater 5000 --column wiki_frequency
        '''
    )
    
    parser.add_argument('--input', default='noun_to_define_with_frequency.xlsx',
                        help='Input Excel file (default: noun_to_define_with_frequency.xlsx)')
    
    parser.add_argument('--output', default='noun_to_define_final.xlsx',
                        help='Output Excel file (default: noun_to_define_final.xlsx)')
    
    parser.add_argument('--column', default='wiki_frequency',
                        help='Column name to filter (default: wiki_frequency)')
    
    # Add mutually exclusive group for operators
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--greater', type=float, metavar='VALUE',
                       help='Filter where column > VALUE')
    group.add_argument('--less', type=float, metavar='VALUE',
                       help='Filter where column < VALUE')
    group.add_argument('--greater-equal', type=float, metavar='VALUE',
                       help='Filter where column >= VALUE')
    group.add_argument('--less-equal', type=float, metavar='VALUE',
                       help='Filter where column <= VALUE')
    group.add_argument('--equal', type=float, metavar='VALUE',
                       help='Filter where column == VALUE')
    
    args = parser.parse_args()
    
    # Determine operator and value
    if args.greater is not None:
        operator, value = '>', args.greater
    elif args.less is not None:
        operator, value = '<', args.less
    elif args.greater_equal is not None:
        operator, value = '>=', args.greater_equal
    elif args.less_equal is not None:
        operator, value = '<=', args.less_equal
    elif args.equal is not None:
        operator, value = '==', args.equal
    
    # Extract the nouns
    extract_nouns(args.input, args.output, args.column, operator, value)

if __name__ == '__main__':
    main()