import Kernel
import commands
import UserHandler
UserH = UserHandler
kernel = Kernel
cmd = commands


def ask():
    global ask_core
    print("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
    ask_core = input("select Mode")


UserH.ask()
print("Go Ahead")
while True:
    kernel.core(MODE=UserH.UserMD)
    if cmd.jump:
        ask()
        print("this is only for the current sension\nthe next time it will be restored\nto the previous state")
        # UserH.Change_Listed_MODE(ask_core)
        cmd.MD = ask_core
        UserH.UserMD = ask_core
        kernel.core(MODE=ask_core)
        cmd.jump = False
    if cmd.jump_user:
        UserH.ask()
        cmd.jump_user = False
        kernel.core(MODE=UserH.UserMD)