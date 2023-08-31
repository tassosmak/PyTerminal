from Kernel.utils import Exit, clear_gui, pl_finder
from Kernel.LoginKit.LoginUI import LoginHandler
from Kernel.RendererKit import Renderer as RD
from Kernel import credentials as cred, flags
from Kernel.SystemCalls import SystemCalls
from Kernel.NotificationsKit import PushSender
from Kernel.AudioKit import Audio
from Kernel.FTU import FTU_init
import sys


def loader(run=True):
    pl_finder()
    clear_gui()
    cred.get_credentials() # <-- if you want to print the credentials set the paramater to True
    if not flags.EnableIntSoft:
        Audio.play('Kernel/AudioKit/src/Boot.mp3')
    if run:
        try:
            if flags.EnableIntSoft:
                cred._get_propiatery(True)
                if flags.UserLess_Connection or flags.GO_TO_FTU:
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

    if cred.FTU in flags.FtuList:
        continue_normal = True
    else:
        if flags.BuildReseted == False:
            FTU = FTU_init()
            FTU.run()
        cred.get_credentials()
        continue_normal = True

    if continue_normal:
        LoginHandler.run()
        if flags.EnableIntSoft:
            PushSender.Sender(f'Login Detected | Username: {flags.USERNAME}')
        
def advanced_init():
    if flags.GO_TO_FTU:
        FTU = FTU_init(False)
        FTU.run()
    flags.USERNAME = "Lets Keep It Private"
    flags.MODE = '9'
    flags.FTU = '1'
    RD.CommandShow(sys.version).Show('GREEN')
    RD.CommandShow(msg="Lets keep it private").Push()