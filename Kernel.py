
import os
import commands
import sys

cmd = commands

def history():
    with open('history.log', 'w+') as f:    
        f.write(str(cmd.LCommand))
                
def core(MODE="0"):
    if MODE == "1":
        cmd.CommandList()
        history()
    elif MODE == "2":
        print("History isn't enabled")
        cmd.CommandList()
    elif MODE == "999":
        passwd = input("pswd:")
        if passwd == "8596":
            print("Acces Granted")
            cmd.CommandList(Admin=True)
    else:
        print("This Mode Doesn't exist")
        sys.exit()