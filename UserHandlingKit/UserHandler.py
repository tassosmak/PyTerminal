import datetime
if not __name__ == '__main__':
    from RendererKit import Renderer as RD
from src import flags
from UserHandlingKit.utils import _pl_finder
from UserHandlingKit import credentials as cred
from UserHandlingKit.FTU import _FTU_init


ask_name = ""
ask_Password = ""
continue_normal = False
correct_pswd_input = False
correct_credentials = False






def _ask(print_ask=False):
    global ask_name, ask_Password
    ask_name = input("Enter Usename")
    ask_Password = input("\nEnter Password")
    if print_ask:
        RD.CommandSay(answer=ask_name)
        RD.CommandSay(answer=ask_Password)




def init():
    _pl_finder()
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
                _ask()
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