from Kernel.RendererKit import Renderer as RD
from Kernel.LoginKit.LoginUI import Login
from Kernel import credentials as cred
from Kernel.utils import pl_finder
from Kernel.FTU import _FTU_init
from Kernel import flags
import datetime
import sys


class init():
    pl_finder()
    cred._get_credentials() # <-- if you want to print the credentials set the paramater to True
    
    def normal_init():
        continue_normal = False
        if not flags.EnableIntSoft:
            try:
                with open('src/history.log', 'a') as f:
                    now = datetime.datetime.now()
                    f.write(now.strftime("%Y-%m-%d %H:%M\n"))
            except FileNotFoundError:
                import os
                os.mkdir('src')
                with open('src/history.log', 'w+') as f:
                    now = datetime.datetime.now()
                    f.write(now.strftime("%Y-%m-%d %H:%M\n"))
                
        if not cred.FTU == "0":
            continue_normal = True
        else:
            if flags.BuildReseted == False:
                _FTU_init()
            cred._get_credentials()
            continue_normal = True

        if continue_normal:
            Login.Verify()
    def advanced_init():
        # _get_propiatery(True)
        if flags.GO_TO_FTU:
            _FTU_init(False)
        flags.FTU = '2'
        flags.USERNAME = "Lets Keep It Private"
        flags.MODE = '9'
        RD.CommandSay(answer=sys.version, color='OKGREEN')
        RD.CommandPush(message="Lets keep it private")

    # print(settings.EnableIntSoft)
    if flags.EnableIntSoft:
        cred._get_propiatery(True)
        if flags.UserLess_Connection == True or flags.GO_TO_FTU == True:
            advanced_init()
        else:
            normal_init()

    else:
        normal_init()