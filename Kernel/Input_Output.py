from Kernel.RendererKit import Renderer as RD
from Kernel import flags


def CommandAsk(Module=str, command=str):
    #MODE 2
    if flags.MODE == "2":
        if flags.Runtype == 'local':
            Module(Command=input(f"{flags.MD2} | {RD.bcolors.OKBLUE}{flags.USERNAME.capitalize()}{RD.bcolors.WHITE} % ").lower())
        elif flags.Runtype == 'gui':
            Module(Command=command)
    #MODE 9
    elif flags.MODE == "9" and flags.BuildReseted == False:
        #GUI
        if flags.Run_Straight_Builtin:
            Module(Command=input(f"{RD.bcolors.WARNING}Run-Straight-Builtin Enabled{RD.bcolors.WHITE} | {flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} % ").lower())
        elif flags.Fully_GUI:
            RD.CommandShow(msg=f"{flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} | Expreimental GUI").Input()
            try: Module(Command=RD.Quest_result.lower())
            except AttributeError: RD.CommandShow('\n').Show()
        #Non GUI
        else:
            if flags.Runtype == 'local':
                Module(Command=input(f"{flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} % ").lower())
            elif flags.Runtype == 'gui':
                Module(Command=command)#(f"{flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} % ").lower())
            
    #Safe Mode
    elif flags.MODE == "3":
        Module(Command=input(f'{RD.bcolors.WARNING}{flags.MD3}{RD.bcolors.WHITE}').lower(), safe_md=True)
        
    #MODE 1
    else:
        Module(Command=input(f"{flags.Default_text} | {RD.bcolors.OKCYAN}{flags.USERNAME.capitalize()}{RD.bcolors.WHITE} $ ").lower())