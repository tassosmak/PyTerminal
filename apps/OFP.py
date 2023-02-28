# OFP --> Out Of PyTerminal
import os
def run():
    command = input('OFP_Terminal: ')
    if not 'zsh' in command:
        os.system(command)

while True:
    try:run()
    except: print('\n')