'''
PyTerminal 
'''
import os
import commands



cmd = commands



def history():
    with open('history.log', 'w') as f:    
        f.write(str(cmd.LCommand))
        
        
def core(MODE="0"):
    if MODE == "1":
        cmd.CommandList()
        history()
    else:
        print("History isn't enabled")
        cmd.CommandList()
        