#!/bin/bash

# Method 1: Run script with visible output
echo "=== Running Claude with output ==="
./auto_claude.sh

# Method 2: Run in background and monitor
# ./auto_claude.sh &
# PID=$!
# echo "Claude script running with PID: $PID"
# echo "Use 'tail -f count.txt' to monitor progress"