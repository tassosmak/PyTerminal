from Kernel.ErrorLoggingKit import Logger as logger
from Kernel.RendererKit import Renderer as RD
from Kernel.AudioKit import Audio
from pathlib import Path
from Kernel import flags
import subprocess
import datetime
import platform
import json
import time
import os

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
        ask_which = input('\n1)Userless Connection\n2)GO TO FTU\n3)Fully GUI\n4)Run-Threads Inside\n\nType Here:')
        
        if ask_which == '1':
            ask_userless_state = input('Enable Or Disable?')
            if ask_userless_state == 'Enable' or ask_userless_state == 'enable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='UserLess Connection', content='1')
                RD.CommandShow('You have to run PyTerminal again for changes to make effect').Show('OKGREEN')
            elif ask_userless_state == 'Disable' or ask_userless_state == 'disable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='UserLess Connection', content='0')
                RD.CommandShow('You have to run PyTerminal again for changes to make effect').Show('OKGREEN')

        elif ask_which == '2':
            ask_ftu_state = input('Enable Or Disable?')
            if ask_ftu_state == 'Enable' or ask_ftu_state == 'enable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='GO TO FTU', content='1')
                RD.CommandShow('You have to run PyTerminal again for changes to make effect').Show('OKGREEN')
            elif ask_ftu_state == 'Disable' or ask_ftu_state == 'disable':
                RD.CommandShow('You have to run PyTerminal again for changes to make effect').Show('OKGREEN')
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='GO TO FTU', content='0')
                
        elif ask_which == '3':
            ask_Fully_GUI_state = input('Enable Or Disable?')
            if ask_Fully_GUI_state == 'Enable' or ask_Fully_GUI_state == 'enable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Fully GUI', content='1')
                RD.CommandShow('You have to run PyTerminal again for changes to make effect').Show('OKGREEN')
            elif ask_Fully_GUI_state == 'Disable' or ask_Fully_GUI_state == 'disable':
                RD.CommandShow('You have to run PyTerminal again for changes to make effect').Show('OKGREEN')
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Fully GUI', content='0')
        
        elif ask_which == '4':
            ask_Inside_Thread = input('Enable Or Disable?')
            if ask_Inside_Thread == 'Enable' or ask_Inside_Thread == 'enable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Run-Threads Inside', content='1')
                RD.CommandShow('You have to run PyTerminal again for changes to make effect').Show('OKGREEN')
            elif ask_Inside_Thread == 'Disable' or ask_Inside_Thread == 'disable':
                RD.CommandShow('You have to run PyTerminal again for changes to make effect').Show('OKGREEN')
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Run-Threads Inside', content='0')

def args_help():
    # RD.CommandSay(answer=(flags.Default_text + '\nThose Are The Available Commands:'), color='BLUE')
    RD.CommandShow(msg=f'{RD.bcolors.OKBLUE}{flags.Default_text}{RD.bcolors.WHITE}\nThose Are The Available Commands:').Show(legacy=True)
    RD.CommandShow(answer=flags.ArgsList).Show("OKGREEN")


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

class SystemCalls:
    
    def get_time(date=True, secs=False):
        now = datetime.datetime.now()
        if date:
            if secs:
                return now.strftime("%Y-%m-%d %H:%M:%S")
            else:
                return now.strftime("%Y-%m-%d %H:%M")
        else:
            return now.strftime("%H:%M")

    def get_folder():
        flags.base_folder = Path(__file__).parent.resolve()
        return flags.base_folder
    
    def get_fl_contents():
        fl_contents = os.listdir(flags.base_folder)
        return fl_contents
    
    def measure_time(func):
        def wrapper():
            pre = time.time()
            func()
            after = time.time() -pre
            after = round(after, 2)
            if flags.MODE == '9':
                RD.CommandShow(msg=f'Time Passed: {after} Seconds').Show('PURPLE')
        return wrapper

    def clear_error():
        pl_finder()
        clear_file = open("Kernel/ErrorLoggingKit/errors.log",'w')
        clear_file.close()
        if flags.pl == '1':
           clear_gui()
        
    def clear_history():
        try:
            clear_file = open(f"{flags.base_folder}/src/history.log",'w')
            clear_file.close()    
        except FileNotFoundError:
            SystemCalls.get_folder()
            clear_file = open(f"{flags.base_folder}/src/history.log",'w')
            clear_file.close()

    def append_to_history(Command):
        if not Command == '0':
            if not 'jump' in Command:
                with open(f'{flags.base_folder}/src/history.log', 'a') as f:
                    f.write(str(f"{Command}\n"))

    def show_flags():
        for arg in flags.all_variables:
            if not arg.startswith('_'):
                value = eval(f'flags.{arg}')
                output = arg, type(value), value
                RD.CommandShow(msg=output).Show(color='BLUE', legacy=True)

def clear_screen():
    if flags.pl == "1" or flags.pl == "3":
        os.system('clear')
    elif flags.pl == '2':
        os.system('cls')
        

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
        flags.EnableIntSoft == False
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