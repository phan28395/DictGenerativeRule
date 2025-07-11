#!/usr/bin/env python3
import pandas as pd
import argparse
import sys

def analyze_nouns(file_path, column_name, operator, value):
    """
    Analyze nouns based on wiki_frequency constraints
    
    Args:
        file_path: Path to the xlsx file
        column_name: Column to filter (e.g., 'wiki_frequency')
        operator: Comparison operator ('>', '<', '>=', '<=', '==')
        value: Threshold value
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
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
        
        # Count unique lemmas
        if 'lemma' in filtered_df.columns:
            unique_lemmas = filtered_df['lemma'].nunique()
            total_entries = len(filtered_df)
            
            print(f"\nResults for {column_name} {operator} {value}:")
            print(f"Number of unique lemmas: {unique_lemmas}")
            print(f"Total entries: {total_entries}")
            
            # Show top 10 entries by frequency
            if len(filtered_df) > 0:
                print(f"\nTop 10 entries by {column_name}:")
                # Sort by frequency in descending order and get top 10
                top_10 = filtered_df.nlargest(10, column_name)
                for i, (_, row) in enumerate(top_10.iterrows(), 1):
                    print(f"  {i}. {row['lemma']:<20} | {column_name}: {row[column_name]:,.0f}")
            
            # Show some sample lemmas
            print(f"\nSample lemmas (first 10):")
            sample_lemmas = filtered_df['lemma'].unique()[:10]
            for i, lemma in enumerate(sample_lemmas, 1):
                print(f"  {i}. {lemma}")
                
        else:
            print("Error: 'lemma' column not found in the Excel file.")
            print(f"Available columns: {', '.join(df.columns)}")
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description='Analyze nouns based on wiki_frequency constraints',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python analyze_nouns_frequency.py --greater 1000
  python analyze_nouns_frequency.py --less 500
  python analyze_nouns_frequency.py --greater-equal 100
  python analyze_nouns_frequency.py --less-equal 2000
  python analyze_nouns_frequency.py --equal 750
        '''
    )
    
    parser.add_argument('--file', default='noun_to_define_with_frequency.xlsx',
                        help='Path to the Excel file (default: noun_to_define_with_frequency.xlsx)')
    
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
    
    # Analyze the nouns
    analyze_nouns(args.file, args.column, operator, value)

if __name__ == '__main__':
    main()