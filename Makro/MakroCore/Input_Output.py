from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags
import os, atexit

if not flags.pl == "2":
    import readline
else:
    import pyreadline3 as readline
 


# Arrow Up functionality
try:
    if flags.FTU == '1':
        HISTORY_FILE = os.path.expanduser("~/.my_python_history")
        if os.path.exists(HISTORY_FILE):
            readline.read_history_file(HISTORY_FILE)
        atexit.register(readline.write_history_file, HISTORY_FILE)
except: pass


def CommandAsk(Module=str):
    if flags.Module == bool:
        import Makro.MakroCore.commands as cmd
        flags.Module = cmd.CommandList
    else:
        # Mode 2
        if flags.MODE == "2":
            prompt = f"{flags.MD2} | {RD.bcolors.OKBLUE}{flags.USERNAME.capitalize()}{RD.bcolors.WHITE} % "
            return Module(Command=input(prompt).lower())

        # Mode 9
        if flags.MODE == "9" and not flags.BuildReseted:
            prompt = f"{flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} | Module Name: {RD.bcolors.OKGREEN}{flags.Module.__name__}{RD.bcolors.WHITE} % "
            if flags.Run_Straight_Builtin:
                msg = f"{RD.bcolors.WARNING}Run-Straight-Builtin Enabled{RD.bcolors.WHITE} | {prompt}"
                return Module(Command=input(msg).lower())
            if flags.Fully_GUI:
                RD.CommandShow(msg=f"{flags.MD9} {flags.sys_detect.system} | {flags.sys_detect.machine} | Expreimental GUI").Input()
                try:
                    return Module(Command=RD.Quest_result.lower())
                except AttributeError:
                    return RD.CommandShow('\n').Show()
            return Module(Command=input(prompt).lower())

        # Safe Mode 3
        if flags.MODE == "3":
            prompt = f'{RD.bcolors.WARNING}{flags.MD3}{RD.bcolors.WHITE}'
            flags.safe_md = True
            return Module(Command=input(prompt).lower())

        # Default Mode 1
        prompt = f"{flags.Default_text} | {RD.bcolors.OKCYAN}{flags.USERNAME.capitalize()}{RD.bcolors.WHITE} $ "
        return Module(Command=input(prompt).lower())