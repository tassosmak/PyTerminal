import Kernel
import commands
import UserHandler
UserH = UserHandler
kernel = Kernel
cmd = commands


while True:
    kernel.core(MODE=UserH.ask_core)
    #cmd.CommandAsk()
    if cmd.jump:
        UserH.ask()
        cmd.MD = UserH.ask_core
        kernel.core(MODE=UserH.ask_core)
        cmd.jump = False
    #print(cmd.jump)