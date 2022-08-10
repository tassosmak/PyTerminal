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
while True:
    print("Go Ahead")
    kernel.core(MODE=UserH.UserMD)
    if cmd.jump:
        ask()
        UserH.Change_Listed_MODE(ask_core)
        cmd.MD = ask_core
        kernel.core(MODE=ask_core)
        cmd.jump = False
    