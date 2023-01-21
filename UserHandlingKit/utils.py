from UserHandlingKit import credentials as cred
from RendererKit import Renderer as RD
from random import shuffle, choice
from src import flags
import platform
import string
import json
from os import system

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
    RD.CommandSay(answer="there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
    ask_core = input("select Mode")
    if ask_core == '9' and flags.EnableIntSoft == False:
        ask_core = '2'
    while not ask_core in flags.ModeList:
        RD.CommandSay(answer="there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
        ask_core = input("select Mode")
        if ask_core in flags.ModeList:
            if ask_core == '9' and flags.EnableIntSoft == False:
                ask_core = '2'
    flags.MODE = ask_core
    RD.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")

def set_flags():
    cred._get_credentials()
    if flags.EnableIntSoft:
        RD.CommandSay(answer='')
        cred._get_propiatery(True)
        RD.CommandSay(answer='')
        ask_which = input('1)Userless Connection\n2)GO TO FTU\nType Here:')
        
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


def clear_error():
    clear_file = open("ErrorLoggingKit/errors.log",'w')
    clear_file.close()
    system('killall osascript')
    
def clear_history():
    clear_file = open("src/history.log",'w')
    clear_file.close()

def args_help():
    RD.CommandSay(answer=flags.ArgsList, color='OKGREEN')


def _pl_finder():
    pl = platform.platform()
    if pl.startswith("macOS"):
        flags.pl = "1"
    elif pl.startswith("Windows"):
        flags.pl = "2"
    elif pl.startswith("Linux"):
        flags.pl = "3"