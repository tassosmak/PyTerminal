import Error_Logger.Logger as logger
import Kernel as kernel
import UserHandler as UserH
import commands as cmd
from src import settings

def ask():
    global ask_core
    print("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
    ask_core = input("select Mode")


def run():    
        try:
            kernel.core(MODE=settings.MODE, pl=settings.pl, username=settings.USERNAME)
        except IndexError:
            ask_new_md = input("it seems that the registered mode of user is corrupted\nwhat mode did you used\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n")
            settings.MODE = ask_new_md
            UserH.edit_json(loc1='user_credentials', loc2='Mode', content=ask_new_md)
        if cmd.jump:
            try:
                UserH.pl_finder()
                ask()
                settings.MODE = ask_core
                try:
                    cmd.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")
                    kernel.core(MODE=ask_core, pl=settings.pl, username=settings.USERNAME)
                except IndexError:
                    ask_corect_md = input("the selected mode doesn't exist These is the available options\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n ")
                    settings.MODE = ask_corect_md
                    kernel.core(MODE=ask_corect_md, pl=settings.pl, username=settings.USERNAME)
                cmd.jump = False
            except NameError:
                    UserH.pl_finder()
                    ask()
                    settings.MODE = ask_core
                    cmd.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")
                    kernel.core(MODE=ask_core, pl=settings.pl, username=settings.USERNAME)
                    cmd.jump = False
        if cmd.jump_user:
            UserH.pl_finder()
            UserH.ask()
            cmd.MD = settings.MODE
            cmd.jump_user = False
            kernel.core(MODE=settings.MODE, pl=settings.pl, username=settings.USERNAME)


UserH.pl_finder()
try:
    UserH.init()
except BaseException:
    settings.MODE = "3"

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
            cmd.CommandSay("There Was An Error", "FAIL")
            from os import system
            system("killall python")