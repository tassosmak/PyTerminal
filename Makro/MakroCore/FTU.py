from Makro.MakroCore.CryptographyKit.utils import _gen_safe_password
from Makro.MakroCore.src import FTU_Installer as ftu_install
from Makro.MakroCore.CryptographyKit import EncryptPassword
from Makro.MakroCore.utils import clear_screen, edit_user_config
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags, SNC, utils
import os, re

class FTU_init:
    
    def __init__(self, edit_use=True):
        self.edit_use = edit_use
        self.type_config = str
        self.username = str
        self.password = str
        self.mode_config = str
    
    def pre_use(self):
        if self.edit_use:
            self.username = 'default'
            edit_user_config(
                username=self.username,
                Loc1='FTU',
                Loc2='Use',
                Content= '1'
                    )
            edit_user_config(
                username=self.username,
                Loc1='user_credentials',
                Loc2='Name',
                Content= 'default'
                    )
            edit_user_config(
                        username=self.username,
                        Loc1='user_credentials',
                        Loc2='Password',
                        Content= 'erydtaiajcjdhcnaberyr1erydtaerydtauicnajdja1uicnajdjauicnajdjaerydtaiajcjdhcnaberyr1erydta1erydtaiajcjdhcnaberyruicnajdjaafsuid'
                    )
            edit_user_config(
                        username=self.username,
                        Loc1='user_credentials',
                        Loc2='Mode',
                        Content= '2'
                    )
            edit_user_config(
                        username=self.username,
                        Loc1='UI',
                        Loc2='Enable-AquaUI',
                        Content= '0'
                    )
            edit_user_config(
                        username=self.username,
                        Loc1='UI',
                        Loc2='Enable-Audio',
                        Content= '0'
                    )
            snc = SNC.snc(self.edit_use)
            snc.guid(self.username)
                
    def use_config(self):
        #use_configure
        utils.clear_screen()
        RD.CommandShow(msg=f"Welcome To {flags.Version} By Anastasios MakroCorestergios\nDon't Wory it an one time only message ;)\n").Show('OKGREEN')
        RD.CommandShow(msg='How Do You want to use this instanche?').Choice(Button1='Minimum', Button2='Full')
        if RD.Quest_result.lower() == 'full' or RD.Quest_result == '1':
            ask_type = '1'
            if self.edit_use:
                if flags.pl == '1':
                    flags.EnableGUI = True
                    flags.EnableAudio = True
        elif RD.Quest_result.lower() == 'minimum' or RD.Quest_result == '2':
            ask_type = '2'
            flags.EnableAudio = False
            flags.EnableGUI = False
            flags.FTU = '2'

        else:
            ask_type = '1'
        if self.edit_use:
            self.type_config = ask_type
        flags.FTU = ask_type
            
    def username_password(self):
        #username_password configuration
        correct_username_input = False
        while not correct_username_input:
            RD.CommandShow(msg='What is your name').Input()
            if not RD.Quest_result in flags.ForbidenUsername:
                self.username = self.username.lower()
                correct_username_input = True
            else:
                RD.CommandShow('this username is not allowed').Info()
            
        self.username = RD.Quest_result
        flags.USERNAME = self.username
    
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

                self.password = EncryptPassword.encrypt_password(password=RD.Quest_result, save=False)
                correct_pswd_input = True
        flags.PASSWORD = self.password
                
    def check(self):
        snc = SNC.snc(self.edit_use)
        snc.guid(self.username)

                
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
            self.mode_config = ask_first_Mode
        flags.MODE = ask_first_Mode

    def dependecies(self):
        #Install_Deperndices
        if self.edit_use:
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
    
    def apply_config(self):
        if self.edit_use:
            apply_done = False
            while not apply_done:
                if os.path.isfile(f'{flags.base_folder}/users/{self.username}.json'):
                    edit_user_config(
                        username=self.username,
                        Loc1='FTU',
                        Loc2='Use',
                        Content= self.type_config
                    )
                    edit_user_config(
                        username=self.username,
                        Loc1='user_credentials',
                        Loc2='Name',
                        Content= self.username
                    ),
                    edit_user_config(
                        username=self.username,
                        Loc1='user_credentials',
                        Loc2='Password',
                        Content= self.password
                    ),
                    edit_user_config(
                        username=self.username,
                        Loc1='user_credentials',
                        Loc2='Mode',
                        Content= self.mode_config
                    )
                    
                    if flags.EnableGUI:
                        edit_user_config(
                            username=self.username,
                            Loc1='UI',
                            Loc2='Enable-AquaUI',
                            Content= '1'
                        )
                    if flags.EnableAudio:
                        edit_user_config(
                            username=self.username,
                            Loc1='UI',
                            Loc2='Enable-Audio',
                            Content= '1'
                        )
                    apply_done = True
                else:
                    open(f'{flags.base_folder}/users/{self.username}.json', 'w+').close()
                    from MakroCore.src import Recover_Json
                    Recover_Json.gen_file(self.username)

    def post_use(self):
        if flags.EnableGUI:
            edit_user_config(
                username='default',
                Loc1='UI',
                Loc2='Enable-AquaUI',
                Content= '1'
            )
        if flags.EnableAudio:
            edit_user_config(
                username='default',
                Loc1='UI',
                Loc2='Enable-Audio',
                Content= '1'
                )
                  
    def run(self):
        self.pre_use()
        self.use_config()
        self.username_password()
        self.check()
        self.mode()
        self.apply_config()
        self.post_use()
        # self.dependecies()