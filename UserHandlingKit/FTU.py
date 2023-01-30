from src import flags
from RendererKit import Renderer as RD
from UserHandlingKit.utils import edit_json, _gen_safe_password, clear_screen
from CryptographyKit import EncryptPassword
import os
from src import FTU_Installer as ftu_install

class _FTU_init:
    def __init__(self, edit_use):
        self.edit_use = edit_use
    
        #check_gui
        if not flags.pl == '1':
            edit_json(loc1='UI', loc2='Enable-AquaUI', content='0')
            flags.EnableGUI = False

        #use_configure
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
        if self.edit_use:
            edit_json(loc1="FTU", loc2="Use", content=ask_type)

        #username_password configuration
        RD.CommandQuest(type='3', msg='What is your name')
        edit_json(loc1="user_credentials", loc2="Name", content=RD.Quest_result)
        
        correct_pswd_input = False
        
        
        while not correct_pswd_input:
            RD.CommandQuest(type='1', msg='Do You Want to to Use A safe Password', Button1='No', Button2='Yes')
            
            
            if RD.Quest_result == 'Yes':
                pre_enc_pswd = _gen_safe_password()
                Password_msg= f'YOUR PASSWORD IS {pre_enc_pswd} KEEP IT SAFE'
                EncryptPassword.encrypt_password(password=pre_enc_pswd)
                RD.CommandQuest(type='2', msg=Password_msg)
                correct_pswd_input = True
            
            
            else:
                RD.CommandQuest(type='3', msg='Type a Password Only Numbers Can Be Entered, No Spaces Or Charachters')
                # EncryptPassword.encrypt_password(password=RD.Quest_result)
                EncryptPassword.encrypt_password(password=RD.Quest_result)
                correct_pswd_input = True
                    
        #Mode_Configuration
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


        #Install_Deperndices
        clear_screen()
        try:
            import rich
        except ModuleNotFoundError:
            ftu_install.install(name="rich")
        try:
            import playwright
        except ModuleNotFoundError:
            ftu_install.install(name="playwright")
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
            import playwright
            import rich
        except ModuleNotFoundError:
            RD.CommandSay("PIP is missing\ncritical features will not work\n Wait a Moment", "FAIL")
            import time
            time.sleep(7)
        os.system('playwright install')
        if not flags.MODE == "9":
            clear_screen()