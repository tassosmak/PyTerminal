from Kernel import flags
from Kernel.RendererKit import Renderer as RD


def CommandAsk(MD='0', safe_mode=False, Module=''):
    if MD == "2":
        Module(Command=input(f"!History isn't enabled! PyTerminal Beta | {flags.USERNAME.capitalize()} % ").lower(), cmd_pl=flags.pl, MD=flags.MODE)
    elif MD == "9" and flags.BuildReseted == False:
        if flags.Fully_GUI:
            RD.CommandQuest(type='3', msg=f"PyTerminal {flags.sys_detect.system} | {flags.sys_detect.machine} | Expreimental GUI") 
            Module(Command=RD.Quest_result.lower(), cmd_pl=flags.pl, MD=flags.MODE)
        else:
            Module(Command=input(f"PyTerminal {flags.sys_detect.system} | {flags.sys_detect.machine} % ").lower(), cmd_pl=flags.pl, MD=flags.MODE)
    elif MD == "3":
        Module(Command=input(f"PyTerminal | Safe-Mode $ ").lower(), cmd_pl=flags.pl, safe_md=safe_mode, MD=flags.MODE)
    else:
        Module(Command=input(f"PyTerminal Beta | {flags.USERNAME.capitalize()} $ ").lower(), cmd_pl=flags.pl, MD=flags.MODE)