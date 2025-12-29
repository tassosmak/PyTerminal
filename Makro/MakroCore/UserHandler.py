from Makro.MakroCore.LoginKit.login_handler import LoginHandler
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import credentials as cred, flags
from Makro.MakroCore.utils import clear_gui, pl_finder
from Makro.MakroCore.SystemCalls import SystemCalls
from Makro.Drivers.AudioKit import Audio
from Makro.MakroCore.FTU import FTU_init
import sys


def loader(run=True):
    pl_finder()
    clear_gui()
    SystemCalls.get_folder()
    if not flags.EnableIntSoft:
        Audio.play('Drivers/AudioKit/src/Boot.mp3')
    if cred._get_propiatery():
        if flags.UserLess_Connection and run:
            advanced_init()
        elif flags.GO_TO_FTU and run:
            FTU = FTU_init(False)
            FTU.run()
        else:
            if run:
                LoginHandler.run()
                init()
            else:
                cred.get_credentials(False, f'{flags.base_folder}/users/default.json')
    else:
        if run:
            LoginHandler.run()
            init()
        else:
            cred.get_credentials(False, f'{flags.base_folder}/users/default.json')
        
def init():
    try:
        with open(f'{flags.base_folder}/src/history.log', 'a') as f:
            f.write(f'\n{SystemCalls.get_time()}')
    except FileNotFoundError:
        from os import mkdir
        mkdir(f'{flags.base_folder}/src')
        with open('src/history.log', 'w+') as f:
            f.write(f'\n{SystemCalls.get_time()}')

        
def advanced_init():
    if flags.pl == '1':
        flags.EnableGUI = True
    flags.EnableIntSoft = True
    flags.USERNAME = "default"
    flags.MODE = '9'
    flags.FTU = '1'
    RD.CommandShow(sys.version).Show('GREEN')
    RD.CommandShow(msg="Lets keep it private").Push()