from Kernel.RendererKit import Renderer as RD
from Kernel import credentials as cred
from Kernel import flags

class LoginHandler():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def Verify(self):
        correct_credentials = False        
        while not correct_credentials:
            if not self.username == "":
                if self.username == cred.Name and self.password == cred.Password:
                    flags.FTU = cred.FTU
                    flags.USERNAME = self.username
                    flags.PASSWORD = self.password
                    welcome_msg = f"Welcome {flags.USERNAME.capitalize()}"
                    RD.CommandPush(message=welcome_msg)
                    RD.CommandSay(answer="Go Ahead")
                    correct_credentials = True
            else:
                flags.MODE = "3"
                correct_credentials = True

    def ask(print_ask=False):
        if flags.Fully_GUI and flags.MODE == '9':
            RD.CommandQuest(type='3', msg='Enter Usename', header=f"{flags.Default_text} Login")
            ask_name = RD.Quest_result
            RD.CommandQuest(type='3', msg='Enter Password', header=f"{flags.Default_text} Login")
            ask_Password = RD.Quest_result
        else:    
            ask_name = input("Enter Usename")
            ask_Password = input("\nEnter Password")
        if print_ask and flags.EnableIntSoft == True:
            RD.CommandSay(f'Typed Username: {ask_name}', 'WARNING')
            RD.CommandSay(f'Typed Password: {ask_Password}', 'WARNING')
        login = LoginHandler(ask_name, ask_Password)
        login.Verify()