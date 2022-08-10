import Kernel
import commands
import UserHandler
UserH = UserHandler
kernel = Kernel
cmd = commands


while True:
    print("Go Ahead")
    UserH.ask()
    if cmd.jump:
        UserH.ask()
        cmd.MD = UserH.UserMD
        kernel.core(MODE=UserH.UserMD)
        cmd.jump = False
    