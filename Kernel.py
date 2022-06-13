
import os
import commands
import sys

cmd = commands

def history():
    with open('history.log', 'w') as f:    
        f.write(str(cmd.LCommand))
                
def core(MODE="0"):
    if MODE == "1":
        cmd.CommandList()
        history()
    elif MODE == "2":
        print("History isn't enabled")
        cmd.CommandList()
    else:
        print("This Mode Doesn't exist")
        sys.exit()