import datetime
if not __name__ == '__main__':
    from RendererKit import Renderer as RD
import platform
import os
import json
import string
from random import shuffle, choice
from src import FTU_Installer as ftu_install, settings
from CryptographyKit import EncryptPassword, DecryptPassword


ask_name = ""
ask_Password = ""
Dresult = ""
continue_normal = False
correct_pswd_input = False
correct_credentials = False
UserLess_Connection = False
GO_TO_FTU = False

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
    global Dresult

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



def _gen_safe_password():
    global final_password
    characters = list(string.digits)
    length = 8
    # length = int(cmd.Quest_result)
    shuffle(characters)
    password = []
    for i in range(length):
        password.append(choice(characters))
    password_str = ''.join(str(e) for e in password)
    final_password = str(password_str)
    # cmd.CommandSay(answer=f'YOUR PASSWORD IS {final_password} keep it safe', color="WARNING")
    _d_encrypt(type='1', input_text=final_password)



def _get_propiatery(print_credentials=False):
    global UserLess_Connection, GO_TO_FTU
    try:
        f = open('MakroPropiatery.json')

        data = json.load(f)

        UserLess_Connection = data['user_login']['UserLess Connection']
        if UserLess_Connection == "1":
            settings.UserLess_Connection = True
        if print_credentials:
            RD.CommandSay(answer=("UserLess Connection:", UserLess_Connection))

        GO_TO_FTU = data['user_login']['GO TO FTU']
        if GO_TO_FTU == "1":
            settings.GO_TO_FTU = True
        if print_credentials:
            RD.CommandSay(answer=("GO_TO_FTU:", GO_TO_FTU))
        f.close()
    except FileNotFoundError:
        pass
    
    

def _get_credentials(print_credentials=False):
    global Name, Password, Mode, FTU, GUI
    try:
        f = open('Info.json')
    except FileNotFoundError:
        try:
            from src import Recover_Json
        except ImportError:
            RD.CommandSay(answer='This Installation is corrupted install a new one', color='FAIL')
            os.system('killall python')
        f = open('Info.json')


    data = json.load(f)

    FTU = data['FTU']['Use']
    if print_credentials:
        RD.CommandSay(answer=("FTU:", FTU))
    
    GUI = data['UI']['Enable-AquaUI']
    if GUI == "1":
        settings.EnableGUI = True
    if print_credentials:
        RD.CommandSay(answer=("UI:", GUI))

    Name = data['user_credentials']['Name']
    if print_credentials:
        RD.CommandSay(answer=("Name:", Name))


    Password = data['user_credentials']['Password']
    _d_encrypt(type='2', input_text=Password)
    Password = Dresult 
    if print_credentials:
        RD.CommandSay(answer=("Password:", Password))


    Internal_Software = data['Internal-Software']['Enable']
    if Internal_Software == "1":
        settings.EnableIntSoft = True
    else: 
        settings.EnableIntSoft = False
    if print_credentials:
        RD.CommandSay(answer=('Settings-Var', settings.EnableIntSoft))
        RD.CommandSay(answer=("Intenal-Software", Internal_Software))
        
    Mode = data['user_credentials']['Mode']
    if settings.EnableIntSoft == False and Mode == '9':
        settings.MODE = '2'
    else:
        settings.MODE = Mode
    if print_credentials:
        RD.CommandSay(answer=("Mode:", Mode))
    
        
    f.close()






def _ask(print_ask=False):
    global ask_name, ask_Password
    ask_name = input("Enter Usename")
    ask_Password = input("\nEnter Password")
    if print_ask:
        RD.CommandSay(answer=ask_name)
        RD.CommandSay(answer=ask_Password)


def _FTU_init(edit_use=True):


    def _check_gui():
        if not settings.pl == '1':
            edit_json(loc1='UI', loc2='Enable-AquaUI', content='0')
            settings.EnableGUI = False

    def _ask_use():
        RD.CommandSay(answer="Welcome To PyTerminal By Tassos Makrostergios\nDon't Wory it an one time only message ;)\n")
        RD.CommandQuest(type='1', Button1='Server', Button2='Personal', ask_admin_msg='How Do You want to use this instanche?')
        #ask_type = input("\n\nHow Do You want to use this instanche?\nPersonal Or Server")
        if RD.Quest_result == 'Personal':
            ask_type = '1'
        elif RD.Quest_result == 'Server':
            ask_type = '2'
            RD.CommandQuest(type='3', quest_msg='Type The ip address you want to send the commands')
            edit_json(loc1="FTU", loc2="IP", content=RD.Quest_result)
        else:
            ask_type = '1'
        if edit_use:
            edit_json(loc1="FTU", loc2="Use", content=ask_type)


    def _ask_name_password():
        RD.CommandQuest(type='3', quest_msg='What is your name')
        edit_json(loc1="user_credentials", loc2="Name", content=RD.Quest_result)
        
        correct_pswd_input = False
        while not correct_pswd_input:
            RD.CommandQuest(type='1', ask_admin_msg='Do You Want to to Use A safe Password', Button1='No', Button2='Yes')
            if RD.Quest_result == 'Yes':
                _gen_safe_password()
                Password_msg= f'YOUR PASSWORD IS {final_password} KEEP IT SAFE'
                RD.CommandQuest(type='2', error_msg=Password_msg)
                correct_pswd_input = True
            else:
                RD.CommandQuest(type='3', quest_msg='Type a Password Only Numbers Can Be Entered, No Spaces Or Charachters')
                if settings.EnableIntSoft:
                    EncryptPassword.password = RD.Quest_result
                    _d_encrypt(type='1', input_text=RD.Quest_result)
                    RD.CommandQuest(type='3', quest_msg='Type a Key')
                    EncryptPassword.encrypt_password(password=EncryptPassword.password, key=RD.Quest_result)
                    correct_pswd_input = True
                    
                elif RD.Quest_result.isdigit():
                    _d_encrypt(type='1', input_text=RD.Quest_result)
                    correct_pswd_input = True


    def _ask_mode():
        RD.CommandQuest(type='1' ,ask_admin_msg='there are 2 Modes on this terminal', Button1='The Advanced Mode', Button2='The Basic Mode')
        if RD.Quest_result == 'The Advanced Mode':
            ask_first_Mode = '2'
        elif RD.Quest_result == 'The Basic Mode':
            ask_first_Mode = '1'
        elif RD.Quest_result == '9':
            ask_first_Mode = '9'
        else:
            ask_first_Mode = '1'
        edit_json(loc1="user_credentials", loc2="Mode", content=ask_first_Mode)



    def _install_dependecies():
        if settings.pl == "1" or settings.pl == "3":
            os.system('clear')
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
            RD.CommandSay("PIP is missing\ncritical features will not work", "FAIL")
            import time
            time.sleep(7)
        if not settings.MODE == "9":
            if settings.pl == "1" or settings.pl == "3":
                os.system('clear')
            elif settings.pl == "2":
                os.system("cls")

    """
    run
    """
    _check_gui()
    _ask_use()
    _ask_name_password()
    _ask_mode()
    _install_dependecies()







def init():
    _pl_finder()
    _get_credentials() # <-- if you want to print the credentials set the paramater to True
    
    def normal_init():
        continue_normal = False
        correct_credentials = False
        if not settings.EnableIntSoft:
            with open('src/history.log', 'a') as f:
                now = datetime.datetime.now()
            f.write(now.strftime("%Y-%m-%d %H:%M\n"))
        if not FTU == "0":
            continue_normal = True
        else:
            _FTU_init()
            _get_credentials()
            continue_normal = True

        if continue_normal:
            while not correct_credentials:
                if settings.EnableIntSoft:
                    DecryptPassword.ask_decrypt()
                    correct_credentials = True
                    settings.FTU = FTU
                    settings.USERNAME = Name
                    welcome_msg = f"Welcome {Name.capitalize()}"
                    RD.CommandPush(message=welcome_msg)
                    RD.CommandSay(answer="Go Ahead")
                else:
                    _ask()
                    if not ask_name == "":
                        if ask_name == Name and ask_Password == Password:
                            correct_credentials = True
                            settings.FTU = FTU
                            settings.USERNAME = ask_name
                            settings.PASSWORD = ask_Password
                            welcome_msg = f"Welcome {Name.capitalize()}"
                            RD.CommandPush(message=welcome_msg)
                            RD.CommandSay(answer="Go Ahead")
                    else:
                        settings.MODE = "3"
                        correct_credentials = True
    def advanced_init():
        # _get_propiatery(True)
        if settings.GO_TO_FTU:
            _FTU_init(False)
        settings.FTU = '2'
        settings.USERNAME = "Lets Keep It Private"
        settings.MODE = '9'
        RD.CommandPush(message="Lets keep it private")

    # print(settings.EnableIntSoft)
    if settings.EnableIntSoft:
        _get_propiatery(True)
        if UserLess_Connection == '1' or GO_TO_FTU == '1':
            advanced_init()
        else:
            normal_init()
    else:
        normal_init()




def _pl_finder():
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