from Kernel.ErrorLoggingKit import Logger as logger
from Kernel.RendererKit import Renderer as RD
from Kernel.AudioKit import Audio
from random import shuffle, choice
from Kernel import flags
import os
import platform
import string
import json

def _reverse_key(text=''):
    str = ""
    for i in text:
        str = i + str
    return str



def edit_json(file_name='Info.json', loc1="", loc2="", content=""):
    with open(file_name, 'r+') as f:
        data = json.load(f)
        if not loc2 == "":
            data[loc1][loc2] = content
        else:
            data[loc1] = content
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()



def _d_encrypt(type=0, input_text=''):
    outstr = "abcdenghik"
    instr = "1234567890"

    if type == "1":
        trans = str.maketrans(instr, outstr)
        final_text = input_text.translate(trans)
        Dresult = _reverse_key(final_text)
        edit_json(loc1='user_credentials', loc2='Password', content=Dresult)
    elif type == '2':
        reverse = str.maketrans(outstr, instr)
        final_text = input_text.translate(reverse)
        Dresult = _reverse_key(final_text)
    return Dresult


def _gen_safe_password(length=8, save=True):
    global final_password
    characters = list(string.digits)
    shuffle(characters)
    password = []
    for i in range(length):
        password.append(choice(characters))
    password_str = ''.join(str(e) for e in password)
    final_password = str(password_str)
    if save:
        _d_encrypt(type='1', input_text=final_password)
    return final_password





def jump_mode():
    if flags.Fully_GUI and flags.MODE == '9':
        RD.CommandQuest(type='3', msg="there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
        ask_core = RD.Quest_result
    else:
        RD.CommandSay(answer='there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode')
        ask_core = input("select Mode")
        if ask_core not in flags.ModeList:
            while not ask_core in flags.ModeList:
                RD.CommandSay(answer="there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
                ask_core = input("select Mode")
                if ask_core in flags.ModeList:
                    if ask_core == '9' and flags.EnableIntSoft == False:
                        ask_core = '2'
        else:
            if ask_core == '9' and flags.EnableIntSoft == False:
                ask_core = '2'
    flags.MODE = ask_core
    flags.jump = False
    RD.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")
            

def set_flags():
        ask_which = input('1)Userless Connection\n2)GO TO FTU\n3)Fully GUI\n4)Run-Threads Inside\nType Here:')
        
        if ask_which == '1':
            ask_userless_state = input('Enable Or Disable?')
            if ask_userless_state == 'Enable' or ask_userless_state == 'enable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='UserLess Connection', content='1')
                RD.CommandSay('You have to run PyTerminal again for changes to make effect', color='OKGREEN')
            elif ask_userless_state == 'Disable' or ask_userless_state == 'disable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='UserLess Connection', content='0')
                RD.CommandSay('You have to run PyTerminal again for changes to make effect', color='OKGREEN')

        elif ask_which == '2':
            ask_ftu_state = input('Enable Or Disable?')
            if ask_ftu_state == 'Enable' or ask_ftu_state == 'enable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='GO TO FTU', content='1')
                RD.CommandSay('You have to run PyTerminal again for changes to make effect', color='OKGREEN')
            elif ask_ftu_state == 'Disable' or ask_ftu_state == 'disable':
                RD.CommandSay('You have to run PyTerminal again for changes to make effect', color='OKGREEN')
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='GO TO FTU', content='0')
                
        elif ask_which == '3':
            ask_Fully_GUI_state = input('Enable Or Disable?')
            if ask_Fully_GUI_state == 'Enable' or ask_Fully_GUI_state == 'enable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Fully GUI', content='1')
                RD.CommandSay('You have to run PyTerminal again for changes to make effect', color='OKGREEN')
            elif ask_Fully_GUI_state == 'Disable' or ask_Fully_GUI_state == 'disable':
                RD.CommandSay('You have to run PyTerminal again for changes to make effect', color='OKGREEN')
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Fully GUI', content='0')
        
        elif ask_which == '4':
            ask_Inside_Thread = input('Enable Or Disable?')
            if ask_Inside_Thread == 'Enable' or ask_Inside_Thread == 'enable':
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Run-Threads Inside', content='1')
                RD.CommandSay('You have to run PyTerminal again for changes to make effect', color='OKGREEN')
            elif ask_Inside_Thread == 'Disable' or ask_Inside_Thread == 'disable':
                RD.CommandSay('You have to run PyTerminal again for changes to make effect', color='OKGREEN')
                edit_json(file_name='MakroPropiatery.json', loc1='user_login', loc2='Run-Threads Inside', content='0')

class Clear:
    def clear_error():
        pl_finder()
        clear_file = open("Kernel/ErrorLoggingKit/errors.log",'w')
        clear_file.close()
        if flags.pl == '1':
            os.system('killall osascript')
        
    def clear_history():
        clear_file = open("src/history.log",'w')
        clear_file.close()

def args_help():
    RD.CommandSay(answer=(flags.Default_text + '\nThose Are The Available Commands:'))
    RD.CommandSay(answer=flags.ArgsList, color='OKGREEN')
    
def error_exit():
    if flags.MODE == "9" or flags.MODE == "3":
        logger.log_error()
        from os import _exit
        _exit(1)
    else:
        if flags.EnableIntSoft:
            logger.log_error("IntSoft Enabled")
            from os import _exit
            _exit(1)
        else:
            RD.CommandSay("There Was An Error", "FAIL")
            Audio.play('Kernel/AudioKit/src/Error.mp3')
            from os import _exit
            _exit(1)
            
def clear_screen():
    if flags.pl == "1" or flags.pl == "3":
        os.system('clear')
    else:
        os.system('cls')

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
        error_exit()