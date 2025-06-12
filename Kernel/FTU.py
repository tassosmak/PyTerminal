from Kernel.CryptographyKit.utils import _gen_safe_password
from Kernel.src import FTU_Installer as ftu_install
from Kernel.CryptographyKit import EncryptPassword
from Kernel.utils import edit_json, clear_screen
from Kernel.RendererKit import Renderer as RD
from Kernel import flags, SNC, utils
import os, re

class FTU_init:
    
    def __init__(self, edit_use=True):
        self.edit_use = edit_use
        
    def check(self):
        snc = SNC.snc(True)
        snc.guid()
        if self.edit_use:
            edit_json(loc1='Internal-Software', loc2='Enable', content='0')
            flags.EnableIntSoft == False
        #check_gui
        if flags.pl == '3':
            edit_json(loc1='UI', loc2='Enable-AquaUI', content='0')
            flags.EnableGUI = False
            
    def use_config(self):
        #use_configure
        utils.clear_screen()
        RD.CommandShow(msg=f"Welcome To {flags.Version} By Anastasios Makrostergios\nDon't Wory it an one time only message ;)\n").Show('OKGREEN')
        RD.CommandShow(msg='How Do You want to use this instanche?').Choice(Button1='Minimum', Button2='Full')
        if RD.Quest_result == 'Full' or RD.Quest_result == '1':
            ask_type = '1'
        elif RD.Quest_result == 'Minimum' or RD.Quest_result == '2':
            ask_type = '2'
            flags.EnableAudio = False
            flags.EnableGUI = False
            flags.FTU = '2'
            if self.edit_use:
                edit_json(loc1='UI', loc2='Enable-AquaUI', content='0')
                edit_json(loc1='UI', loc2='Enable-Audio', content='0')
        else:
            ask_type = '1'
        if self.edit_use:
            edit_json(loc1="FTU", loc2="Use", content=ask_type)
            
    def username_password(self):
        #username_password configuration
        RD.CommandShow(msg='What is your name').Input()
        edit_json(loc1="user_credentials", loc2="Name", content=RD.Quest_result)
    
        correct_pswd_input = False
        while not correct_pswd_input:
            RD.CommandShow(msg='Do you want us to create a password for you?').Choice(Button1='No', Button2='Yes')
            
            if RD.Quest_result.lower() == 'yes':
                pre_enc_pswd = _gen_safe_password()
                Password_msg= f'YOUR PASSWORD IS {pre_enc_pswd} KEEP IT SAFE'
                EncryptPassword.encrypt_password(password=pre_enc_pswd)
                RD.CommandShow(msg=Password_msg).Info()
                correct_pswd_input = True
                            
            else:
                RD.CommandShow(msg='Type a Password Only Numbers Can Be Entered, No Spaces Or Special Charachters').Input()
                
                #remove spaces and special characters
                RD.Quest_result.replace(' ', '')
                RD.Quest_result = re.sub(r'[^a-zA-Z0-9]', '', RD.Quest_result)

                EncryptPassword.encrypt_password(password=RD.Quest_result)
                correct_pswd_input = True
    def mode(self):
        #Mode_Configuration
        RD.CommandShow(msg='there are 2 Modes on this terminal').Choice(Button1='The Advanced Mode', Button2='The Basic Mode')
        if RD.Quest_result == 'The Advanced Mode' or RD.Quest_result == '2':
            ask_first_Mode = '2'
        elif RD.Quest_result == 'The Basic Mode' or RD.Quest_result == '1':
            ask_first_Mode = '1'
        elif RD.Quest_result == '9':
            ask_first_Mode = '9'
        else:
            ask_first_Mode = '1'
        if self.edit_use:
            edit_json(loc1="user_credentials", loc2="Mode", content=ask_first_Mode)
        flags.MODE = ask_first_Mode

    def dependecies(self):
        #Install_Deperndices
        clear_screen()
        num = 0
        try:
            if flags.MODE == '9':
                RD.CommandShow('--Dependecies Install Start--\n').Show(color='WARNING')
            while len(flags.Dependecies) > num:
                utils.progress_bar(
                    module=ftu_install.install,
                    arg1=flags.Dependecies[num],
                    arg2=flags.EnableIntSoft,
                    description=f'Dependecy Installer Num.{num} {flags.Dependecies[num]}'
                )
                num += 1
            os.system('playwright install')
            RD.CommandShow(msg='All Dependecies Installed Successfully').Push()
            if flags.MODE == '9':
                RD.CommandShow('\n--Dependecies Install End--\n').Show('WARNING')
        except MemoryError:
            RD.CommandShow(msg='Error Occured While installing dependecies').Show()
        
        if not flags.MODE == "9":
            clear_screen()
            
    def run(self):
        self.check()
        self.use_config()
        self.username_password()
        self.mode()
        self.dependecies()