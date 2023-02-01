from Kernel import credentials as cred
from Kernel.utils import pl_finder
from Kernel.RendererKit import Renderer as RD
from Kernel.FTU import _FTU_init
from Kernel import flags
import datetime
import sys


def _ask(print_ask=False):
    ask_name = input("Enter Usename")
    ask_Password = input("\nEnter Password")
    if print_ask:
        RD.CommandSay(answer=ask_name)
        RD.CommandSay(answer=ask_Password)
    return ask_name, ask_Password




def init():
    pl_finder()
    cred._get_credentials() # <-- if you want to print the credentials set the paramater to True
    
    def normal_init():
        continue_normal = False
        correct_credentials = False
        if not flags.EnableIntSoft:
            with open('src/history.log', 'a') as f:
                now = datetime.datetime.now()
                f.write(now.strftime("%Y-%m-%d %H:%M\n"))
        if not cred.FTU == "0":
            continue_normal = True
        else:
            _FTU_init()
            cred._get_credentials()
            continue_normal = True

        if continue_normal:
            while not correct_credentials:
                ask_name, ask_Password = _ask()
                if not ask_name == "":
                    if ask_name == cred.Name and ask_Password == cred.Password:
                        flags.FTU = cred.FTU
                        flags.USERNAME = ask_name
                        flags.PASSWORD = ask_Password
                        welcome_msg = f"Welcome {flags.USERNAME.capitalize()}"
                        RD.CommandPush(message=welcome_msg)
                        RD.CommandSay(answer="Go Ahead")
                        correct_credentials = True
                else:
                    flags.MODE = "3"
                    correct_credentials = True
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