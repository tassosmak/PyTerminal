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
            kernel.core(MODE=settings.MODE, pl=settings.pl, username=UserH.username_ask)
        except IndexError:
            ask_new_md = input("it seems that the registered mode of user is corrupted\nwhat mode did you used\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n")
            settings.MODE = ask_new_md
            UserH.Change_Listed_MODE(ask_new_md)
        if cmd.jump:
            try:
                UserH.pl_finder()
                ask()
                settings.MODE = ask_core
                try:
                    kernel.core(MODE=ask_core, pl=settings.pl, username=UserH.username_ask)
                except IndexError:
                    ask_corect_md = input("the selected mode doesn't exist These is the available options\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n ")
                    settings.MODE = ask_corect_md
                    kernel.core(MODE=ask_corect_md, pl=settings.pl, username=UserH.username_ask)
                cmd.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")
                cmd.jump = False
            except NameError:
                    UserH.pl_finder()
                    ask()
                    settings.MODE = ask_core
                    cmd.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")
                    kernel.core(MODE=ask_core, pl=settings.pl, username=UserH.username_ask)
                    cmd.jump = False
        if cmd.jump_user:
            UserH.pl_finder()
            UserH.ask()
            cmd.MD = UserH.UserMD
            cmd.jump_user = False
            kernel.core(MODE=settings.MODE, pl=settings.pl, username=UserH.username_ask)


UserH.pl_finder()
UserH.init()
counter = 0
try:
    UserH.ask()
except BaseException:
    UserH.UserMD = "3"
    restrict_jump = True

cmd.CommandSay(answer="Go Ahead")
def boot():
    try:
        #print(UserH.UserMD)
        run()
    except KeyboardInterrupt:
        print("\n")
        pass
    except BaseException:
        if UserH.UserMD == "9" or UserH.UserMD == "3":
            cmd.CommandSay("There Was An Error see 'errors.log' in the Error_Manager Folder for more info", "FAIL")
            logger.log_error()
            from os import system
            system("killall python")
        else:
            cmd.CommandSay("There Was An Error", "FAIL")
            from os import system
            system("killall python")