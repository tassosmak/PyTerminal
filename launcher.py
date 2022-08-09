import Kernel
import commands
kernel = Kernel
cmd = commands

def ask():
    global ask_core
    print("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
    ask_core = input("select Mode")
jump = cmd.jump
ask()
cmd.MD = ask_core
print("Go Ahead")
while True:
    #kernel.core(MODE=ask_core)
    cmd.CommandAsk()
    