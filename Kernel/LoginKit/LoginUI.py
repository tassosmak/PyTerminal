from Kernel.RendererKit import Renderer as RD
from Kernel import credentials as cred
from Kernel import flags





class Login:
    correct_credentials = False
    
    def ask(print_ask=False):
        if flags.Fully_GUI and flags.MODE == '9':
            RD.CommandQuest(type='3', msg='Enter Usename')
            ask_name = RD.Quest_result
            RD.CommandQuest(type='3', msg='Enter Password')
            ask_Password = RD.Quest_result
        else:    
            ask_name = input("Enter Usename")
            ask_Password = input("\nEnter Password")
        if print_ask:
            RD.CommandSay(answer=ask_name)
            RD.CommandSay(answer=ask_Password)
        return ask_name, ask_Password

    def Verify():
        while not Login.correct_credentials:
            ask_name, ask_Password = Login.ask()
            if not ask_name == "":
                if ask_name == cred.Name and ask_Password == cred.Password:
                    flags.FTU = cred.FTU
                    flags.USERNAME = ask_name
                    flags.PASSWORD = ask_Password
                    welcome_msg = f"Welcome {flags.USERNAME.capitalize()}"
                    RD.CommandPush(message=welcome_msg)
                    RD.CommandSay(answer="Go Ahead")
                    Login.correct_credentials = True
            else:
                flags.MODE = "3"
                Login.correct_credentials = True