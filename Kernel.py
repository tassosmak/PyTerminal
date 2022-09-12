import commands
import sys

cmd = commands


def history():
    with open('history.log', 'a') as f:    
        f.write(str(f"{cmd.LCommand}\n"))
                
def core(MODE="0", pl=0):
    if MODE == "1":
        cmd.MD = MODE
        cmd.CommandAsk(plt=pl)
        history()
    elif MODE == "2":
        print("History isn't enabled")
        cmd.MD = MODE
        cmd.CommandAsk(plt=pl)
    elif MODE == "9":
        cmd.MD = MODE
        cmd.CommandAsk(Admin=True, plt=pl)
    else:
        raise IndexError