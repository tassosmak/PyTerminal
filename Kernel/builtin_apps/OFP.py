# OFP --> Out Of PyTerminal
import os
def run():
    command = input('OFP_Terminal: ')
    if not 'exit' in command:
        if not 'zsh' in command:
            os.system(command)
    else:
        from os import _exit
        _exit(1)

while True:
    try:run()
    except: print('\n')