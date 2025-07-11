#!/usr/bin/env python3

import sys

print("Manual trigger for noun generation")
print("-" * 50)

# Read current count
try:
    with open("count.txt", "r") as f:
        content = f.read().strip()
        current = int(content.split("x=")[1]) if "x=" in content else 0
except:
    current = 0

print(f"Current count: {current}")

# Ask user how many to trigger
if len(sys.argv) > 1:
    increase = int(sys.argv[1])
else:
    increase = 20

new_count = current + increase

print(f"Will update count to: {new_count} (increase of {increase})")
print("This will trigger the monitor to generate entries...")

# Update count
with open("count.txt", "w") as f:
    f.write(f"x={new_count}")

print(f"✓ Updated count.txt to x={new_count}")
print("The monitor will now start generating entries!")