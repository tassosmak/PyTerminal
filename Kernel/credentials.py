from Kernel.CryptographyKit import DecryptPassword
from Kernel.RendererKit import Renderer as RD
from Kernel import utils, flags, SNC
import json
import os


def _get_propiatery(print_credentials=False):
    global UserLess_Connection, GO_TO_FTU, Fully_GUI
    f = open('MakroPropiatery.json')

    data = json.load(f)
    try:
        UserLess_Connection = data['user_login']['UserLess Connection']
    except KeyError:
        raise FileNotFoundError
    if UserLess_Connection == "1":
        flags.UserLess_Connection = True
    if print_credentials:
        RD.CommandSay(answer=("UserLess Connection:", UserLess_Connection))

    try:
        GO_TO_FTU = data['user_login']['GO TO FTU']
    except KeyError:
        raise FileNotFoundError
    if GO_TO_FTU == "1":
        flags.GO_TO_FTU = True
    if print_credentials:
        RD.CommandSay(answer=("GO_TO_FTU:", GO_TO_FTU))
        
    try:
        Fully_GUI = data['user_login']['Fully GUI']
    except KeyError:
        raise FileNotFoundError
    if Fully_GUI == "1" and flags.EnableGUI and flags.pl == '1':
        flags.Fully_GUI = True
    if print_credentials:
        RD.CommandSay(answer=("Fully_GUI:", Fully_GUI))
    
    try:
        Inside_Thread = data['user_login']['Run-Threads Inside']
    except KeyError:
        raise FileNotFoundError
    if Inside_Thread == "1":
        flags.Inside_Thread = True
    if print_credentials:
        RD.CommandSay(answer=("Run-Threads Inside:", Inside_Thread))
    f.close()

    
    
Name = 0
Password = 0
Mode = 0
FTU = 0
GUI = 0
SerialNum = 0
def _get_credentials(print_credentials=False):
    utils.get_folder()
    global Name, Password, Mode, FTU, GUI, SerialNum
    try:
        f = open('Info.json')
    except FileNotFoundError:
        try:
            from Kernel.src import Recover_Json
        except ImportError:
            RD.CommandSay(answer='This Installation is corrupted install a new one', color='FAIL')
            os._exit(1)
        f = open('Info.json')


    data = json.load(f)

    FTU = data['FTU']['Use']
    flags.FTU = FTU
    if print_credentials:
        RD.CommandSay(answer=("FTU:", FTU))
    
    GUI = data['UI']['Enable-AquaUI']
    if GUI == "1":
        flags.EnableGUI = True
    if print_credentials:
        RD.CommandSay(answer=("UI:", GUI))
    
    Audio = data['UI']['Enable-Audio']
    if Audio == "1":
        flags.EnableAudio = True
    if print_credentials:
        RD.CommandSay(answer=("Audio:", GUI))

    Name = data['user_credentials']['Name']
    if print_credentials:
        RD.CommandSay(answer=("Name:", Name))


    Password = data['user_credentials']['Password']
    Password = DecryptPassword.decrypt_password(password=Password)
    if print_credentials:
        RD.CommandSay(answer=("Password:", Password))


    Internal_Software = data['Internal-Software']['Enable']
    try:
        _get_propiatery()
        if Internal_Software == "1":
            flags.EnableIntSoft = True
        else: 
            flags.EnableIntSoft = False
    except FileNotFoundError:
        flags.EnableIntSoft == False
    if print_credentials:
        RD.CommandSay(answer=('Settings-Var', flags.EnableIntSoft))
        RD.CommandSay(answer=("Intenal-Software", Internal_Software))
        
    Mode = data['user_credentials']['Mode']
    if flags.EnableIntSoft == False and Mode == '9':
        flags.MODE = '2'
    else:
        flags.MODE = Mode
    if print_credentials:
        RD.CommandSay(answer=("Mode:", Mode))
        
    SerialNum = data['user_credentials']['Serial']
    try:
        SNC.guid()
    except IndexError:
        if flags.EnableIntSoft:
            RD.CommandSay("The Serial number of the computer doesn't match the doesn't match the serial number given", 'FAIL')
        utils.Clear.clear_error()
        utils.Clear.clear_history()
        from Kernel.FTU import _FTU_init
        _FTU_init()
        flags.BuildReseted = True
    if print_credentials:
        RD.CommandSay(answer=("Serial:", SerialNum))
    
        
    f.close()
