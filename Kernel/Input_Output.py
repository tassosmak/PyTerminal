from Kernel import flags
from Kernel.RendererKit import Renderer as RD


def CommandAsk(MD='0', safe_mode=False, Module=''):
    #MODE 2
    if MD == "2":
        Module(Command=input(f"{flags.MD2} | {flags.USERNAME.capitalize()} % ").lower(), cmd_pl=flags.pl, MD=flags.MODE)
        
    #MODE 9
    elif MD == "9" and flags.BuildReseted == False:
        #GUI
        if flags.Fully_GUI:
            RD.CommandQuest(type='3', msg=f"{flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} | Expreimental GUI") 
            Module(Command=RD.Quest_result.lower(), cmd_pl=flags.pl, MD=flags.MODE)
        #Non GUI
        else:
            Module(Command=input(f"{flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} % ").lower(), cmd_pl=flags.pl, MD=flags.MODE)
            
    #Safe Mode
    elif MD == "3":
        Module(Command=input(flags.MD3).lower(), cmd_pl=flags.pl, safe_md=safe_mode, MD=flags.MODE)
        
    #MODE 1
    else:
        Module(Command=input(f"{flags.Default_text} | {flags.USERNAME.capitalize()} $ ").lower(), cmd_pl=flags.pl, MD=flags.MODE)