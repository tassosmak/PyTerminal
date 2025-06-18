from Kernel import credentials as cred, flags, InputManagerKit
from Kernel.NotificationsKit.PushSender import Notifications
from Kernel.CryptographyKit import EncryptPassword
from Kernel.RendererKit import Renderer as RD
from Kernel.FTU import FTU_init as FTU
import os 

class LoginHandler():
    def __init__(self):
        self.username = str
        self.password = str
    
    def welcome_prompt(self):
        welcome_msg = f"Welcome {flags.USERNAME.capitalize()}"
        RD.CommandShow(welcome_msg).Push()
        RD.CommandShow("Go Ahead").Show()
        


    
    def ask_username(self, print_ask=False):
        if flags.Fully_GUI and flags.MODE == '9':
            ask_name = RD.CommandShow(msg='Enter Usename', header="Login").Input()
        else:
            ask_name = input("Enter Username")
        if print_ask and flags.EnableIntSoft == True:
            RD.CommandShow(f'Typed Username: {ask_name}').Show('WARNING')
        return ask_name
    
    def ask_password(self, print_ask=False):
        if flags.Fully_GUI and flags.MODE == '9':
            ask_Password = EncryptPassword.encrypt_password(RD.CommandShow(msg='Enter Password', header="Login").Input(), save=False)
        else:    
            ask_Password = EncryptPassword.encrypt_password(InputManagerKit.askpass("\nEnter Password"), save=False)
        if print_ask and flags.EnableIntSoft == True:
            RD.CommandShow(f'Typed Password: {EncryptPassword.decrypt_password(ask_Password)}').Show('WARNING')
        return ask_Password
    

    def Verify_User_Exists(self):
        if os.path.exists(f'{flags.base_folder}/users/'): 
            self.correct_credentials = False
            while not self.correct_credentials:
                self.username = self.ask_username()
                self.path = f'{flags.base_folder}/users/{self.username}.json'
                if not self.username == "":
                    if os.path.isfile(self.path):
                        cred.get_credentials(False, self.path)
                        if self.username == cred.Name:
                            flags.USERNAME = self.username
                            self.password = self.ask_password()
                            if self.password == cred.Password:
                                flags.PASSWORD = self.password
                                self.correct_credentials = True
                else:
                    flags.MODE = "3"
                    self.correct_credentials = True
        else:
            os.makedirs(f'{flags.base_folder}/users')
            FTU(edit_use=True).run()
    
    def two_step_verification(self):
        self.verified = False
        if not flags.pl == '2':
            self.code = Notifications().Code_Sender()
            while not self.verified:
                if flags.Fully_GUI and flags.MODE == '9':
                    self.ask_code = RD.CommandShow('We Have Send A code to your Phone').Input()
                    if self.ask_code == self.code:
                        self.verified = True
                else:
                    self.ask_code = input('We Have Send A code to your Phone')
                    if self.ask_code == self.code:
                        self.verified = True
        else: 
            RD.CommandShow("Development Mode isn't supported on Windows").Show('WARNING')
            flags.EnableIntSoft = False
    

        
    def run():
        Login = LoginHandler()
        Login.Verify_User_Exists()
        if flags.EnableIntSoft:
            Login.two_step_verification()
        Login.welcome_prompt()