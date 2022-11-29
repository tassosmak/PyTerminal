import datetime
import commands as cmd
import platform
import os
import json
from src import FTU_Installer as ftu_install, settings


ask_name = ""
ask_Password = ""
Dresult = ""
continue_normal = False

correct_credentials = False

def reverse_key(text=''):
    str = ""
    for i in text:
        str = i + str
    return str
  


def edit_json(file_name="Info.json", loc1="", loc2="", content=""):
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
    global Dresult

    outstr = "abcdenghik"
    instr =  "1234567890" 

    if type == "1":
        trans = str.maketrans(instr, outstr)
        final_text = input_text.translate(trans)
        Dresult = reverse_key(final_text)
        edit_json(loc1='user_credentials', loc2='Password', content=Dresult)
    elif type == '2':
        reverse = str.maketrans(outstr, instr)
        final_text = input_text.translate(reverse)
        Dresult = reverse_key(final_text)





def get_credentials(print_credentials=False):
    global Name, Password, Mode, FTU, GUI
    f = open('Info.json')

    data = json.load(f)

    FTU = data['FTU']['Use']
    if print_credentials:
        cmd.CommandSay(answer=("FTU:", FTU))
    
    GUI = data['UI']['Enable-AquaUI']
    if GUI == "1":
        settings.EnableGUI = True
    if print_credentials:
        cmd.CommandSay(answer=("UI:", GUI))

    Name = data['user_credentials']['Name']
    if print_credentials:
        cmd.CommandSay(answer=("Name:", Name))


    Password = data['user_credentials']['Password']
    _d_encrypt(type='2', input_text=Password)
    Password = Dresult 
    if print_credentials:
        cmd.CommandSay(answer=("Password:", Password))


    Mode = data['user_credentials']['Mode']
    settings.MODE = Mode
    if print_credentials:
        cmd.CommandSay(answer=("Mode:", Mode))
    
    Internal_Software = data['Internal-Software']['Enable']
    if Internal_Software == "1":
        settings.EnableIntSoft = True
    else: 
        settings.EnableIntSoft = False
    if print_credentials:
        cmd.CommandSay(answer=('Settings-Var', settings.EnableIntSoft))
        cmd.CommandSay(answer=("Intenal-Software", Internal_Software))

    f.close()






def ask(print_ask=False):
    global ask_name, ask_Password
    ask_name = input("Enter Usename")
    ask_Password = input("\nEnter Password")
    if print_ask:
        cmd.CommandSay(answer=ask_name)
        cmd.CommandSay(answer=ask_Password)


def FTU_init():
    cmd.CommandSay(answer="Welcome To PyTerminal By Tassos Makrostergios\nDon't Wory it an one time only message ;)\n")
    cmd.CommandQuest(type='1', Button1='Personal', Button2='Server', ask_admin_msg='How Do You want to use this instanche?')
    #ask_type = input("\n\nHow Do You want to use this instanche?\nPersonal Or Server")
    if cmd.Quest_result == 'Personal':
        ask_type = '1'
    elif cmd.Quest_result == 'Server':
        ask_type = '2'
    else:
        ask_type = '1'
    edit_json(loc1="FTU", loc2="Use", content=ask_type)
    
    cmd.CommandQuest(type='3', quest_msg='What is your name')
    ask_first_name = cmd.Quest_result
    
    cmd.CommandQuest(type='3', quest_msg='Type a Password')
    _d_encrypt(type='1', input_text=cmd.Quest_result)
    ask_first_Password = Dresult


    cmd.CommandQuest(type='1' ,ask_admin_msg='there are 2 Modes on this terminal', Button1='The Advanced Mode', Button2='The Basic Mode')
    if cmd.Quest_result == 'The Advanced Mode':
        ask_first_Mode = '2'
    elif cmd.Quest_result == 'The Basic Mode':
        ask_first_Mode = '1'
    elif cmd.Quest_result == '9':
        ask_first_Mode = '9'
    else:
        ask_first_Mode = '1'
    



    edit_json(loc1="user_credentials", loc2="Name", content=ask_first_name)
    edit_json(loc1="user_credentials", loc2="Password", content=ask_first_Password)
    edit_json(loc1="user_credentials", loc2="Mode", content=ask_first_Mode)
    if settings.pl == "1" or settings.pl == "3":
        os.system("clear")
    elif settings.pl == "2":
        os.system("cls")
    try:
        import pyrad
    except ModuleNotFoundError:
        ftu_install.install(name="pyrad")
    try:
        import clipboard
    except ModuleNotFoundError:
        ftu_install.install(name="clipboard")
    try:
        import pyrad
        import clipboard
    except ModuleNotFoundError:       
        cmd.CommandSay("PIP is missing\ncritical features will not work", "FAIL")
        import time
        time.sleep(7)
    if not settings.MODE == "9":
        if settings.pl == "1" or settings.pl == "3":
            os.system("clear")
        elif settings.pl == "2":
            os.system("cls")









def init():
    continue_normal = False
    correct_credentials = False
    with open('src/history.log', 'a') as f:    
        now = datetime.datetime.now()
        f.write(now.strftime("%Y-%m-%d %H:%M\n"))
    get_credentials() # <-- if you want to print the credentials set the paramater to True
    if not FTU == "0":
        continue_normal = True
    else:
        FTU_init()
        get_credentials()
        continue_normal = True

    if continue_normal:
        while not correct_credentials:
            ask()
            if not ask_name == "":
                if ask_name == Name and ask_Password == Password:
                    correct_credentials = True
                    settings.FTU = FTU
                    settings.USERNAME = ask_name
                    settings.PASSWORD = ask_Password
                    welcome_msg = f"Welcome {Name.capitalize()}"
                    cmd.CommandPush(message=welcome_msg)
            else:
                settings.MODE = "3"
                correct_credentials = True













def pl_finder():
    global pl
    pl = platform.platform()
    if pl.startswith("macOS"):
        #os.system("killall python")
        pl = "1"
    elif pl.startswith("Windows"):
        pl = "2"
    elif pl.startswith("Linux"):
        #os.system("killall python")
        pl = "3"
    settings.pl = pl
