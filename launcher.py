import Kernel
import commands
import UserHandler

kernel = Kernel
cmd = commands
UserH = UserHandler
UserH_WSH = UserH.WorkSpaceHandler

def ask():
    global ask_core
    print("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
    ask_core = input("select Mode")




UserH_WSH.init()
UserH.ask()
cmd.CommandSay(answer="Go Ahead")
def run():
    while True:
            try:
                kernel.core(MODE=UserH.UserMD)
            except IndexError:
                ask_new_md = input("it seems that the registered mode of user is corrupted\nwhat mode did you used\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n")
                UserH.Change_Listed_MODE(ask_new_md)
                kernel.core(MODE=ask_new_md)
            if cmd.jump:
                ask()
                cmd.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")
                # UserH.Change_Listed_MODE(ask_core)
                cmd.MD = ask_core
                UserH.UserMD = ask_core
                kernel.core(MODE=ask_core)
                cmd.jump = False
            if cmd.jump_user:
                UserH.ask()
                cmd.jump_user = False
                kernel.core(MODE=UserH.UserMD)
while True:
    try:
        run()
    except KeyboardInterrupt:
        pass
