import Error_Logger.Logger as logger
import Kernel as kernel
import commands as cmd
import UserHandler as UserH

def ask():
    global ask_core
    print("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
    ask_core = input("select Mode")


def run():    
        try:
            kernel.core(MODE=UserH.UserMD, pl=UserH.pl, username=UserH.username)
        except IndexError:
            ask_new_md = input("it seems that the registered mode of user is corrupted\nwhat mode did you used\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n")
            UserH.Change_Listed_MODE(ask_new_md)
            kernel.core(MODE=ask_new_md, pl=UserH.pl, username=UserH.username)
        if cmd.jump:
            UserH.pl_finder()
            ask()
            cmd.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")
            cmd.MD = ask_core
            UserH.UserMD = ask_core
            kernel.core(MODE=ask_core, pl=UserH.pl, username=UserH.username)
            cmd.jump = False
        if cmd.jump_user:
            UserH.pl_finder()
            UserH.ask()
            cmd.MD = UserH.UserMD
            cmd.jump_user = False
            kernel.core(MODE=UserH.UserMD, pl=UserH.pl, username=UserH.username)


UserH.pl_finder()
UserH.init()
UserH.ask()
cmd.CommandSay(answer="Go Ahead")
def boot():
    try:
        #print(UserH.UserMD)
        run()
    except KeyboardInterrupt:
        print("\n")
        pass
    except BaseException:
        if UserH.UserMD == "9":
            cmd.CommandSay("There Wan Error see 'errors.log' in the Error_Manager Folder for more info", "FAIL")
            logger.log_error()
            import sys
            sys.exit()
        else:
            cmd.CommandSay("There Wan Error", "FAIL")
            import sys
            sys.exit()