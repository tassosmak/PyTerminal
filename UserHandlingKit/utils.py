import json
import string
from random import shuffle, choice
import platform
from src import settings
from RendererKit import Renderer as RD

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
    if ask_core == '9' and settings.EnableIntSoft == False:
        ask_core = '2'
    while not ask_core in settings.ModeList:
        RD.CommandSay(answer="there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
        ask_core = input("select Mode")
        if ask_core in settings.ModeList:
            if ask_core == '9' and settings.EnableIntSoft == False:
                ask_core = '2'
    settings.MODE = ask_core
    RD.CommandSay(answer="this is only for the current sension\nthe next time it will be restored\nto the previous state", color="WARNING")



def _pl_finder():
    pl = platform.platform()
    if pl.startswith("macOS"):
        settings.pl = "1"
    elif pl.startswith("Windows"):
        settings.pl = "2"
    elif pl.startswith("Linux"):
        settings.pl = "3"