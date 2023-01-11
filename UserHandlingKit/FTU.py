from src import settings
from RendererKit import Renderer as RD
from UserHandlingKit.utils import edit_json, _gen_safe_password, _d_encrypt
from CryptographyKit import EncryptPassword
import os
from src import FTU_Installer as ftu_install

def _FTU_init(edit_use=True):

    def _check_gui():
        if not settings.pl == '1':
            edit_json(loc1='UI', loc2='Enable-AquaUI', content='0')
            settings.EnableGUI = False

    def _ask_use():
        RD.CommandSay(answer="Welcome To PyTerminal By Tassos Makrostergios\nDon't Wory it an one time only message ;)\n")
        RD.CommandQuest(type='1', Button1='Server', Button2='Personal', msg='How Do You want to use this instanche?')
        #ask_type = input("\n\nHow Do You want to use this instanche?\nPersonal Or Server")
        if RD.Quest_result == 'Personal':
            ask_type = '1'
        elif RD.Quest_result == 'Server':
            ask_type = '2'
            RD.CommandQuest(type='3', msg='Type The ip address you want to send the commands')
            edit_json(loc1="FTU", loc2="IP", content=RD.Quest_result)
        else:
            ask_type = '1'
        if edit_use:
            edit_json(loc1="FTU", loc2="Use", content=ask_type)


    def _ask_name_password():
        RD.CommandQuest(type='3', msg='What is your name')
        edit_json(loc1="user_credentials", loc2="Name", content=RD.Quest_result)
        
        correct_pswd_input = False
        
        
        while not correct_pswd_input:
            RD.CommandQuest(type='1', msg='Do You Want to to Use A safe Password', Button1='No', Button2='Yes')
            
            
            if RD.Quest_result == 'Yes':
                pre_enc_pswd = _gen_safe_password()
                Password_msg= f'YOUR PASSWORD IS {EncryptPassword.encrypt_password(password=pre_enc_pswd)} KEEP IT SAFE'
                RD.CommandQuest(type='2', msg=Password_msg)
                correct_pswd_input = True
            
            
            else:
                RD.CommandQuest(type='3', msg='Type a Password Only Numbers Can Be Entered, No Spaces Or Charachters')
                EncryptPassword.encrypt_password(password=RD.Quest_result)
                correct_pswd_input = True
                    
                    
    def _ask_mode():
        RD.CommandQuest(type='1', msg='there are 2 Modes on this terminal', Button1='The Advanced Mode', Button2='The Basic Mode')
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
            RD.CommandSay("PIP is missing\ncritical features will not work\n Wait a Moment", "FAIL")
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