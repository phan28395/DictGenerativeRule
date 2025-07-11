#!/bin/bash

# Script to create named terminals in VS Code
# Usage: Run this script in VS Code's integrated terminal

# Create terminals for each folder
echo "Creating named terminals for noun generation..."

# Terminal 1: Folder 1-500
code --new-window --goto "lemmas_to_define/1 to 500" &
sleep 1

# Terminal 2: Folder 501-1000
code --new-window --goto "lemmas_to_define/501 to 1000" &
sleep 1

# Terminal 3: Folder 1001-1500
code --new-window --goto "lemmas_to_define/1001 to 1500" &
sleep 1

# Terminal 4: Folder 1501-2000
code --new-window --goto "lemmas_to_define/1501 to 2000" &

echo "Terminals created. You can now rename them manually in VS Code."