#!/usr/bin/env python3

import subprocess
import sys
import os

# Detect the terminal emulator
def get_terminal_command():
    # Try common terminal emulators in order of preference
    terminals = [
        ['gnome-terminal', '--', 'bash', '-c'],
        ['konsole', '-e', 'bash', '-c'],
        ['xfce4-terminal', '-e', 'bash -c'],
        ['xterm', '-e', 'bash', '-c'],
        ['terminator', '-e', 'bash', '-c'],
    ]
    
    for terminal in terminals:
        try:
            # Check if terminal exists
            subprocess.run(['which', terminal[0]], capture_output=True, check=True)
            return terminal
        except:
            continue
    
    print("No suitable terminal emulator found!")
    return None

print("Launching Noun Generator Monitor in new terminal window...")

# Get the terminal command
terminal_cmd = get_terminal_command()
if not terminal_cmd:
    sys.exit(1)

# Get the directory path
script_dir = os.path.dirname(os.path.abspath(__file__))
monitor_script = os.path.join(script_dir, 'auto_noun_generator.py')

# Command to run in the new terminal
run_command = f"cd '{script_dir}' && python3 '{monitor_script}'; echo 'Press Enter to close...'; read"

# Launch the terminal
cmd = terminal_cmd + [run_command]
subprocess.Popen(cmd)

print("✓ Monitor launched in new terminal window!")
print("You can now use start_generation.py to trigger generations.")
print("\nTo trigger the first batch, run:")
print("  python start_generation.py")