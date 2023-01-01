from src import settings
from RendererKit import Renderer as RD
import json
import os
from UserHandlingKit.utils import _d_encrypt


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
    
    
Name = 0
Password = 0
Mode = 0
FTU = 0
GUI = 0
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
    Password = _d_encrypt(type='2', input_text=Password)
        
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
