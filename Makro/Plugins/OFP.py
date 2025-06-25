from src import utils
utils.add_depend(str(utils.sys.argv[1]))
from MakroCore import flags

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
if flags.EnableIntSoft:
    while True:
        try:run()
        except: print('\n')