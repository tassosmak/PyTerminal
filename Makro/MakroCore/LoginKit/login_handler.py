from Makro.MakroCore.LoginKit.two_step_verification import TwoStepVerification
from Makro.MakroCore.LoginKit.LoginUI import LoginHandlerUserStore
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags


class LoginHandler():
    def __init__(self):
        self.username = str
        self.password = str
        self.correct_credentials = False
        self.verified = False
        self.user_store = LoginHandlerUserStore()
        self.verifier = TwoStepVerification()

    def welcome_prompt(self):
        welcome_msg = f"Welcome {flags.USERNAME.capitalize()}"
        RD.CommandShow(welcome_msg).Push()
        RD.CommandShow("Go Ahead").Show()

    def Verify_User_Exists(self):
        self.user_store.Verify_User_Exists()

    def two_step_verification(self):
        self.verifier.two_step_verification()


    def run():
        Login = LoginHandler()
        Login.Verify_User_Exists()
        if flags.EnableIntSoft:
            Login.two_step_verification()
        Login.welcome_prompt()