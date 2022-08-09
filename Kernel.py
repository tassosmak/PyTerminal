import os
import commands
import sys

cmd = commands



def history():
    with open('history.log', 'w+') as f:    
        f.write(str(cmd.LCommand))
                
def core(MODE="0"):
    if MODE == "1":
        cmd.CommandAsk()
        history()
    elif MODE == "2":
        print("History isn't enabled")
        cmd.CommandAsk()
    elif MODE == "999":
        passwd = input("pswd:")
        if passwd == "8596":
            print("Acces Granted")
            cmd.CommandAsk(Admin=True)
    else:
        print("This Mode Doesn't exist")
        sys.exit()