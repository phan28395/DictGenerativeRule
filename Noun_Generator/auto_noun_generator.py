#!/usr/bin/env python3

import os
import time
import subprocess
import json
from pathlib import Path

class NounGeneratorMonitor:
    def __init__(self):
        self.count_file = Path("count.txt")
        self.last_count = None
        self.batch_size = 20
        
    def read_count(self):
        """Read the current count from count.txt"""
        try:
            with open(self.count_file, 'r') as f:
                content = f.read().strip()
                # Extract the number after 'x='
                if 'x=' in content:
                    return int(content.split('x=')[1])
                return 0
        except Exception as e:
            print(f"Error reading count: {e}")
            return 0
    
    def write_count(self, new_count):
        """Write the updated count back to count.txt"""
        try:
            with open(self.count_file, 'w') as f:
                f.write(f"x={new_count}")
        except Exception as e:
            print(f"Error writing count: {e}")
    
    def generate_entries_batch(self, start_row, end_row):
        """Generate entries for rows from start_row to end_row"""
        entries_to_generate = min(20, end_row - start_row)
        print(f"\n📋 Generating {entries_to_generate} entries (rows {start_row + 1} to {start_row + entries_to_generate})")
        
        for i, row in enumerate(range(start_row + 1, start_row + entries_to_generate + 1), 1):
            print(f"\n[{i}/{entries_to_generate}] Generating entry for row {row}...")
            
            # Construct the claude command
            prompt = f'''Based on the file Noun_Rule_Final.md, generate entry with the structure outlined in JSON-Schema.json and add to the JSON-File Noun-Entries.json for the Lemma in column "Lemma" at the row {row} in the file noun_to_define_final.xlsx'''
            
            # Call claude using subprocess in non-interactive mode
            try:
                print(f"   → Calling claude CLI...")
                result = subprocess.run(
                    ['claude', '-p', prompt],
                    capture_output=True,
                    text=True,
                    check=True
                )
                print(f"   ✓ Entry for row {row} generated successfully")
                print(f"   → Output length: {len(result.stdout)} characters")
                
                # Update count after each successful generation
                self.write_count(row)
                print(f"   ✓ Updated count to {row}")
                
                # Small delay to avoid overwhelming the system
                time.sleep(2)
                
            except subprocess.CalledProcessError as e:
                print(f"   ✗ Error generating entry for row {row}: {e}")
                print(f"   → Error output: {e.stderr}")
                print(f"   → Return code: {e.returncode}")
                break
            except Exception as e:
                print(f"   ✗ Unexpected error for row {row}: {e}")
                break
        
        print(f"\n✓ Batch complete. Generated {i} entries.")
    
    def monitor(self):
        """Main monitoring loop"""
        print("Starting Noun Generator Monitor...")
        print(f"Monitoring {self.count_file} for changes...")
        print(f"Will trigger generation every {self.batch_size} count increases")
        print("-" * 50)
        
        # Initialize with current count
        self.last_count = self.read_count()
        print(f"Initial count: {self.last_count}")
        
        while True:
            try:
                current_count = self.read_count()
                
                # Check if count has increased by batch_size
                if current_count >= self.last_count + self.batch_size:
                    print(f"\n🔔 Count increased from {self.last_count} to {current_count}")
                    print(f"Generating {self.batch_size} entries...")
                    
                    # Generate entries for the batch
                    self.generate_entries_batch(self.last_count, current_count)
                    
                    # Update last count
                    self.last_count = current_count
                    print(f"Batch complete. Current count: {current_count}")
                    print("-" * 50)
                
                # Check every 5 seconds
                time.sleep(5)
                
            except KeyboardInterrupt:
                print("\n\nMonitoring stopped by user.")
                break
            except Exception as e:
                print(f"Error in monitoring loop: {e}")
                time.sleep(5)

if __name__ == "__main__":
    monitor = NounGeneratorMonitor()
    monitor.monitor()