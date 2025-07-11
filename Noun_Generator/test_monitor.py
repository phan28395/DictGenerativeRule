#!/usr/bin/env python3

import time

print("Test script to simulate count increases")
print("This will update count.txt to trigger the monitor")
print("-" * 50)

# Read current count
try:
    with open("count.txt", "r") as f:
        content = f.read().strip()
        current = int(content.split("x=")[1]) if "x=" in content else 0
except:
    current = 0

print(f"Current count: {current}")
print(f"Will update to: {current + 20}")
print("Updating in 3 seconds...")
time.sleep(3)

# Update count to trigger monitor
new_count = current + 20
with open("count.txt", "w") as f:
    f.write(f"x={new_count}")

print(f"✓ Updated count.txt to x={new_count}")
print("The monitor should now detect this change and start generating entries!")