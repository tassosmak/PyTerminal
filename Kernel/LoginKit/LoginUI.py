from Kernel.RendererKit import Renderer as RD
from Kernel import credentials as cred, flags
from Kernel.CryptographyKit import EncryptPassword

class LoginHandler():
    def __init__(self):
        pass
    
    def Verify(self):
        self.correct_credentials = False
        while not self.correct_credentials:
            self.username, self.password = self.ask()
            if not self.username == "":
                if self.username == cred.Name and self.password == cred.Password:
                    flags.FTU = cred.FTU
                    flags.USERNAME = self.username
                    flags.PASSWORD = self.password
                    welcome_msg = f"Welcome {flags.USERNAME.capitalize()}"
                    RD.CommandShow(welcome_msg).Push()
                    RD.CommandShow("Go Ahead").Show()
                    self.correct_credentials = True
            else:
                flags.MODE = "3"
                self.correct_credentials = True

    def ask(self, print_ask=False):
        if flags.Fully_GUI and flags.MODE == '9':
            ask_name = RD.CommandShow(msg='Enter Usename', header=f"{flags.Default_text} Login").Input()
            ask_Password = RD.CommandShow(msg='Enter Password', header=f"{flags.Default_text} Login").Input()
        else:    
            ask_name = input("Enter Usename")
            ask_Password = EncryptPassword.encrypt_password(input("\nEnter Password"), save=False)
        if print_ask and flags.EnableIntSoft == True:
            RD.CommandShow(f'Typed Username: {ask_name}').Show('WARNING')
            RD.CommandShow(f'Typed Password: {ask_Password}').Show('WARNING')
        return ask_name, ask_Password
    
    def run():
        Login = LoginHandler()
        Login.Verify()