from Kernel import flags
from Kernel.RendererKit import Renderer as RD


def CommandAsk(Module=''):
    #MODE 2
    if flags.MODE == "2":
        Module(Command=input(f"{flags.MD2} | {flags.USERNAME.capitalize()} % ").lower())
        
    #MODE 9
    elif flags.MODE == "9" and flags.BuildReseted == False:
        #GUI
        if flags.Fully_GUI:
            RD.CommandQuest(type='3', msg=f"{flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} | Expreimental GUI") 
            Module(Command=RD.Quest_result.lower())
        #Non GUI
        else:
            Module(Command=input(f"{flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} % ").lower())
            
    #Safe Mode
    elif flags.MODE == "3":
        Module(Command=input(flags.MD3).lower(), safe_md=True)
        
    #MODE 1
    else:
        Module(Command=input(f"{flags.Default_text} | {flags.USERNAME.capitalize()} $ ").lower())