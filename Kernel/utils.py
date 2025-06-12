from Kernel.ErrorLoggingKit import Logger as logger
from Kernel.RendererKit import Renderer as RD
from Kernel.AudioKit import Audio
from Kernel import flags
import subprocess
import platform
import json
import os
from Kernel.RendererKit.ProgressBarKit import tqdm

def edit_json(file_name=f'Info.json', loc1="", loc2="", content=""):
    with open(file_name, 'r+') as f:
        data = json.load(f)
        if not loc2 == "":
            data[loc1][loc2] = content
        else:
            data[loc1] = content
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def set_flags():
        ask_which = input('\n1)Userless Connection\n2)GO TO FTU\n3)Fully GUI\n4)Run-Threads Inside\n5)Run-Straight-Builtin\n6)Create_Graph\n7)Runtime_Tracer\n\nType Here:')
        
        if ask_which == '1':
            flags.UserLess_Connection = not flags.UserLess_Connection
            edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='UserLess Connection', content=flags.UserLess_Connection)

        elif ask_which == '2':
            flags.GO_TO_FTU = not flags.GO_TO_FTU
            edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='GO TO FTU', content=flags.GO_TO_FTU)
                
        elif ask_which == '3':
            flags.Fully_GUI = not flags.Fully_GUI
            edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Fully GUI', content=flags.Fully_GUI)
        
        elif ask_which == '4':
            flags.Inside_Thread = not flags.Inside_Thread
            edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Run-Threads Inside', content=flags.Inside_Thread)
  
        elif ask_which == '5':
            flags.Run_Straight_Builtin = not flags.Run_Straight_Builtin
            edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Run-Straight-Builtin', content=flags.Run_Straight_Builtin)

        elif ask_which == '6':
            flags.Create_Graph = not flags.Create_Graph
            edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Create_Graph', content=flags.Create_Graph)
                
        elif ask_which == '7':
            flags.Runtime_Tracer = not flags.Runtime_Tracer
            edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Runtime_Tracer', content=flags.Runtime_Tracer)

def args_help():
    # RD.CommandSay(msg=(flags.Default_text + '\nThose Are The Available Commands:'), color='BLUE')
    RD.CommandShow(msg=f'{RD.bcolors.OKBLUE}{flags.Default_text}{RD.bcolors.WHITE}\nThose Are The Available Commands:').Show(legacy=True)
    RD.CommandShow(msg=flags.ArgsList).Show("OKGREEN")


class Exit:
    def error_exit():
        # pass
        if flags.MODE == "9" or flags.MODE == "3":
            logger.log_error()
            Exit.exit()
        else:
            if flags.EnableIntSoft:
                logger.log_error("IntSoft Enabled")
                Exit.exit()
            else:
                RD.CommandShow("There Was An Error").Show('FAIL')
                Audio.play('Kernel/AudioKit/src/Error.mp3')
                Exit.exit()
                
    def exit():
        os._exit(1)

def clear_screen():
    if flags.pl == "1" or flags.pl == "3":
        os.system('clear')
    elif flags.pl == '2':
        os.system('cls')

def progress_bar(module=str, arg1=str, arg2=str, description=str):
    if not description==flags.Default_text:
                description=f'{flags.Default_text} | {description}'
    for i in tqdm(arg1, desc=description):
        module(arg1, arg2)


def clear_gui():
    if not flags.pl == str:
        if flags.pl == '1':
            try:
                subprocess.run('killall osascript', shell=True, capture_output=True , check=True, encoding="utf-8")
            except: pass
    else:
        RD.CommandShow('You have to run pl_finder to clear the gui').Show('WARNING')
        
class ModeHandling:
    def recover_mode():
        flags.EnableIntSoft = False
        while not RD.Quest_result in flags.ModeList:
            RD.CommandShow(msg="It Seems That The Registered Mode Is Corrupted\nWhat Mode Did You Used\n\n1) The Basic Mode\n2) The Advanced Mode", header=f'Mode Recovery').Input()
        if RD.Quest_result == '9':
            RD.Quest_result = '2'
        flags.MODE = RD.Quest_result
        edit_json(loc1='user_credentials', loc2='Mode', content=flags.MODE)
        edit_json(loc1='Internal-Software', loc2='Enable', content='0')
        
    def jump_mode():
        ask_core = str
        if flags.Fully_GUI and flags.MODE == '9':
            ask_core = RD.CommandShow(msg="there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode").Choice(Button1='1', Button2='2')
        else:
            while not ask_core in flags.ModeList:
                try:
                    RD.CommandShow("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode").Show()
                    ask_core = input("Select Mode")
                    if ask_core == '9' and flags.EnableIntSoft == False:
                            ask_core = '2'
                except EOFError:
                    continue

        flags.MODE = ask_core
        flags.jump = False
        RD.CommandShow("this is only for the current sension\nthe next time it will be restored\nto the previous state").Show('WARNING')

def pl_finder():
    pl = platform.platform()
    if pl.startswith("macOS"):
        flags.sys_detect = platform.uname()
        flags.pl = "1"
    elif pl.startswith("Windows"):
        flags.sys_detect = platform.uname()
        flags.pl = "2"
    elif pl.startswith("Linux"):
        flags.sys_detect = platform.uname()
        flags.pl = "3"
    else:
        Exit.error_exit()