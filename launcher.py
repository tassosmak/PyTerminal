import Error_Logger.Logger as logger
if not __name__ == '__main__':
    import Kernel as kernel
    import UserHandler as UserH
    import commands as cmd
from src import settings

def ask():
    global ask_core
    print("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
    ask_core = input("select Mode")
    if ask_core == '9' and settings.EnableIntSoft == False:
        ask_core = '2'


def run():    
        try:
            kernel.core(MODE=settings.MODE, pl=settings.pl, username=settings.USERNAME)
        except IndexError:
            ask_new_md = input("it seems that the registered mode of user is corrupted\nwhat mode did you used\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n")
            settings.MODE = ask_new_md
            UserH.edit_json(loc1='user_credentials', loc2='Mode', content=ask_new_md)
            UserH.edit_json(loc1='Internal-Software', loc2='Enable', content='0')
        if cmd.jump:
            ask()
            settings.MODE = ask_core
            try:
                cmd.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")
                if settings.EnableIntSoft:
                    kernel.core(MODE=settings.MODE, pl=settings.pl, username=settings.USERNAME)
                else:
                    kernel.core(MODE=settings.MODE, pl=settings.pl, username=settings.USERNAME)
            except IndexError:
                ask_corect_md = input("the selected mode doesn't exist These is the available options\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n ")
                settings.MODE = ask_corect_md
                if settings.EnableIntSoft:
                    kernel.core(MODE=settings.MODE, pl=settings.pl, username=settings.USERNAME)
                else:
                    kernel.core(MODE=settings.MODE, pl=settings.pl, username=settings.USERNAME)
            cmd.jump = False



if not __name__ == '__main__':
    UserH.init()
    cmd.CommandSay(answer="Go Ahead")

def boot():
    try:
        #print(UserH.UserMD)
        run()
    except KeyboardInterrupt:
        print("\n")
        pass
    except BaseException:
        if settings.MODE == "9" or settings.MODE == "3":
            cmd.CommandSay("There Was An Error see 'errors.log' in the Error_Manager Folder for more info", "FAIL")
            logger.log_error()
            from os import system
            system("killall python")
        else:
            if settings.EnableIntSoft:
                logger.log_error("IntSoft Enabled")
            cmd.CommandSay("There Was An Error", "FAIL")
            from os import system
            system("killall python")