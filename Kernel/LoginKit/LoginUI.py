from Kernel import credentials as cred, flags, InputManagerKit
from Kernel.CryptographyKit import EncryptPassword, utils
from Kernel.NotificationsKit import PushSender
from Kernel.RendererKit import Renderer as RD

class LoginHandler():
    def __init__(self):
        pass
    
    def welcome_prompt(self):
        welcome_msg = f"Welcome {flags.USERNAME.capitalize()}"
        RD.CommandShow(welcome_msg).Push()
        RD.CommandShow("Go Ahead").Show()
        
    def Verify(self):
        self.correct_credentials = False
        while not self.correct_credentials:
            self.username, self.password = self.ask()
            if not self.username == "":
                if self.username == cred.Name and self.password == cred.Password:
                    flags.FTU = cred.FTU
                    flags.USERNAME = self.username
                    flags.PASSWORD = self.password
                    self.correct_credentials = True
            else:
                flags.MODE = "3"
                self.correct_credentials = True

    def ask(self, print_ask=False):
        if flags.Fully_GUI and flags.MODE == '9':
            ask_name = RD.CommandShow(msg='Enter Usename', header="Login").Input()
            ask_Password = RD.CommandShow(msg='Enter Password', header="Login").Input()
        else:    
            ask_name = input("Enter Usename")
            ask_Password = EncryptPassword.encrypt_password(InputManagerKit.askpass("\nEnter Password"), save=False)
        if print_ask and flags.EnableIntSoft == True:
            RD.CommandShow(f'Typed Username: {ask_name}').Show('WARNING')
            # RD.CommandShow(f'Typed Password: {DecryptPassword.decrypt_password(ask_Password)}').Show('WARNING')
        return ask_name, ask_Password
    
    def two_step_verification(self):
        def check_platform():
            if flags.pl == '2':
                RD.CommandShow("The Development Environment isn't supported on Windows\nYou Will be moved down to the Advanced Mode").Push()
                flags.EnableIntSoft = False
                return False
        if check_platform() == True:
            self.verified = False
            self.code = utils._gen_safe_password(4)
            PushSender.Sender(self.code)
            while not self.verified:
                # self.ask_code = RD.CommandShow('We Have Send A code to your Phone').Input()
                self.ask_code = input('We Have Send A code to your Phone')
                if self.ask_code == self.code:
                    self.verified = True
    

        
    def run():
        Login = LoginHandler()
        Login.Verify()
        # if flags.EnableIntSoft:
            # Login.two_step_verification()
        Login.welcome_prompt()