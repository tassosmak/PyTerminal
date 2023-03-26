from Kernel.utils import Exit, clear_gui, SystemCalls, pl_finder
from Kernel import credentials as cred, flags
from Kernel.RendererKit import Renderer as RD
from Kernel.LoginKit.LoginUI import LoginHandler
from Kernel.AudioKit import Audio
from Kernel.FTU import FTU_init
import sys


def loader(run=True):
    pl_finder()
    clear_gui()
    cred._get_credentials() # <-- if you want to print the credentials set the paramater to True
    if not flags.EnableIntSoft:
        Audio.play('Kernel/AudioKit/src/Boot.mp3')
    if run:
        try:
            if flags.EnableIntSoft:
                cred._get_propiatery(True)
                if flags.UserLess_Connection == True or flags.GO_TO_FTU == True:
                    advanced_init()
                else:
                    init()
            else:
                init()
        except:
            Exit.error_exit()

        
def init():
    continue_normal = False
    if not flags.EnableIntSoft:
        try:
            with open(f'{flags.base_folder}/src/history.log', 'a') as f:
                f.write(f'\n{SystemCalls.get_time()}')
        except FileNotFoundError:
            from os import mkdir
            mkdir(f'{flags.base_folder}/src')
            with open('src/history.log', 'w+') as f:
                f.write(f'\n{SystemCalls.get_time()}')

    if not cred.FTU == "0":
        continue_normal = True
    else:
        if flags.BuildReseted == False:
            FTU = FTU_init()
            FTU.run()
        cred._get_credentials()
        continue_normal = True

    if continue_normal:
        LoginHandler.run()
        
def advanced_init():
    if flags.GO_TO_FTU:
        FTU = FTU_init(False)
        FTU.run()
    flags.USERNAME = "Lets Keep It Private"
    flags.MODE = '9'
    flags.FTU = '1'
    RD.CommandSay(answer=sys.version, color='OKGREEN')
    RD.CommandPush(message="Lets keep it private")