from Kernel.RendererKit import Renderer as RD
from Kernel.SystemCalls import SystemCalls
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
        RD.CommandShow(msg=("UserLess Connection:", UserLess_Connection)).Show()

    try:
        GO_TO_FTU = data['user_login']['GO TO FTU']
    except KeyError:
        raise FileNotFoundError
    if GO_TO_FTU == "1":
        flags.GO_TO_FTU = True
    if print_credentials:
        RD.CommandShow(msg=("GO_TO_FTU:", GO_TO_FTU)).Show()
        
    try:
        Fully_GUI = data['user_login']['Fully GUI']
    except KeyError:
        raise FileNotFoundError
    if Fully_GUI == "1" and flags.EnableGUI and flags.pl == '1':
        flags.Fully_GUI = True
    if print_credentials:
        RD.CommandShow(msg=("Fully_GUI:", Fully_GUI)).Show()
    
    try:
        Inside_Thread = data['user_login']['Run-Threads Inside']
    except KeyError:
        raise FileNotFoundError
    if Inside_Thread == "1":
        flags.Inside_Thread = True
    if print_credentials:
        RD.CommandShow(msg=("Run-Threads Inside:", Inside_Thread)).Show()
    
    try:
        Run_Straight_Builtin = data['user_login']['Run-Straight-Builtin']
    except KeyError:
        raise FileNotFoundError
    if Run_Straight_Builtin == "1":
        flags.Run_Straight_Builtin = True
    if print_credentials:
        RD.CommandShow(msg=("Run_Straight_Builtin:", Run_Straight_Builtin)).Show()
    f.close()

    
    
Name = 0
Password = 0
Mode = 0
FTU = 0
GUI = 0
SerialNum = 0
def _get_credentials(print_credentials=False):
    SystemCalls.get_folder()
    global Name, Password, Mode, FTU, GUI, SerialNum
    try:
        f = open(f'{flags.base_folder}/../Info.json')
    except FileNotFoundError:
        try:
            from Kernel.src import Recover_Json
        except ImportError:
            RD.CommandShow(msg='This Installation is corrupted install a new one').Show('FAIL')
            os._exit(1)
        f = open('Info.json')


    data = json.load(f)

    FTU = data['FTU']['Use']
    flags.FTU = FTU
    if print_credentials:
        RD.CommandShow(msg=("FTU:", FTU)).Show()
    
    GUI = data['UI']['Enable-AquaUI']
    if GUI == "1":
        flags.EnableGUI = True
    if print_credentials:
        RD.CommandShow(msg=("UI:", GUI)).Show()
    
    Audio = data['UI']['Enable-Audio']
    if Audio == "1":
        flags.EnableAudio = True
    if print_credentials:
        RD.CommandShow(msg=("Audio:", GUI)).Show()

    Name = data['user_credentials']['Name']
    if print_credentials:
        RD.CommandShow(msg=("Name:", Name)).Show()


    Password = data['user_credentials']['Password']
    flags.PASSWORD = Password
    if print_credentials:
        if flags.EnableIntSoft:
            RD.CommandShow(msg=("Password:", Password)).Show()
    # Password = DecryptPassword.decrypt_password(password=Password)


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
        if flags.EnableIntSoft:
            RD.CommandShow(msg=('Flags-Var', flags.EnableIntSoft)).Show()
            RD.CommandShow(msg=("Intenal-Software", Internal_Software)).Show()
        
    Mode = data['user_credentials']['Mode']
    if flags.EnableIntSoft == False and Mode == '9':
        flags.MODE = '2'
    else:
        flags.MODE = Mode
    if print_credentials:
        RD.CommandShow(msg=("Mode:", Mode)).Show()
        
    SerialNum = data['user_credentials']['Serial']
    try:
        snc = SNC.snc()
        snc.guid()
    except IndexError:
        if flags.EnableIntSoft:
            RD.CommandShow("The Serial number of the computer doesn't match the serial number given").Show('FAIL')
        utils.SystemCalls.clear_error()
        utils.SystemCalls.clear_history()
        from Kernel.FTU import FTU_init
        FTU_init(True).run()
        flags.BuildReseted = True
    if print_credentials:
        RD.CommandShow(msg=("Serial:", SerialNum)).Show()
    
        
    f.close()
