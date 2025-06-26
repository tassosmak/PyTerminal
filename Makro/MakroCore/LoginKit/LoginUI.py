from Makro.MakroCore import credentials as cred, flags
from Makro.Drivers import InputManagerKit
try:
    from Makro.MakroCore.CryptographyKit.decrypt import Decryptor
except ModuleNotFoundError:pass
from Makro.MakroCore.CryptographyKit import EncryptPassword
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore.FTU import FTU_init as FTU
from Makro.MakroCore import utils
import os


class LoginHandlerUserStore:
    def ask_username(self, print_ask=False):
        if flags.Fully_GUI and flags.MODE == '9':
            ask_name = RD.CommandShow(msg='Type Username: ', header="Login").Input()
        else:
            ask_name = input("Type Username: ")
        if print_ask and flags.EnableIntSoft == True:
            RD.CommandShow(f'Typed Username: {ask_name}').Show('WARNING')
        return ask_name

    def ask_password(self, print_ask=False):
        if flags.Fully_GUI and flags.MODE == '9':
            ask_Password = EncryptPassword.encrypt_password(
                RD.CommandShow(msg='Type Password:', header="Login").Input(), save=False)
        else:
            ask_Password = EncryptPassword.encrypt_password(InputManagerKit.askpass("\nType Password: "), save=False)
        if print_ask and flags.EnableIntSoft == True:
            try:
                RD.CommandShow(f'Typed Password: {Decryptor.decrypt_password(ask_Password)}').Show('WARNING')
            except ModuleNotFoundError:
                pass
        return ask_Password

    def Verify_User_Exists(self):
        if os.path.exists(f'{flags.base_folder}/users/'):
            correct_credentials = False
            while not correct_credentials:
                utils.clear_screen()
                username = self.ask_username()
                path = f'{flags.base_folder}/users/{username}.json'
                if username != "":
                    if username not in flags.ForbidenUsername:
                        if os.path.isfile(path):
                            cred.get_credentials(False, path)
                            if username == cred.Name:
                                flags.USERNAME = username
                                password = self.ask_password()
                                if password == cred.Password:
                                    flags.PASSWORD = password
                                    correct_credentials = True
                else:
                    flags.MODE = "3"
                    flags.USERNAME = "Native-Mode"
                    correct_credentials = True
        else:
            os.makedirs(f'{flags.base_folder}/users')
            FTU(edit_use=True).run()