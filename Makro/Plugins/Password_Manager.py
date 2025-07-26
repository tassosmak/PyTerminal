import json, os

from src.utils import add_depend, sys
add_depend(str(sys.argv[1]))

from Makro.MakroCore.CryptographyKit import EncryptPassword as EP
from Makro.MakroCore.CryptographyKit.decrypt import Decryptor
from Makro.MakroCore.FlagsCaller import CallHandler as CH
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore.JSONhander import JSONhandle

class PasswordManager:
    
    def __init__(self):
        self.file_path = f'{CH.get_base_folder()}/../Plugins/src/pwdfile.json'
        self.username = str
        self.password = str
        self.filename = str
        
    def manage_file(self, name: str, username: str, password: str):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as recover:
                try:
                    data = json.load(recover)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}

        data[name] = {
            "Name": username,
            "Password": password
        }

        with open(self.file_path, 'w') as recover:
            json.dump(data, recover, indent=4)

                                                                                                                                                                                         
    def add_password(self):
        self.filename = RD.CommandShow('Give a name for the login').Input()
        self.username = RD.CommandShow("Type the Username Of the Passwords You Want to Add").Input()
        
        self.password = RD.CommandShow("Type the Passwords You Want to Add").Input()
        correct_pwd = False
        while not correct_pwd:
            confirm_password = RD.CommandShow("Confirm the Password").Input()
            if confirm_password == self.password:
                correct_pwd = True
            else:
                RD.CommandShow("Passwords do not match, please try again.").Info()
        self.password = EP.encrypt_password(self.password, False)
        self.manage_file(self.filename, self.username, self.password)

    
    def view_passwords(self):
        correct_name = False
        while correct_name == False:
            self.filename = RD.CommandShow("Enter the name of the Usesname/Password Combo you want to view").Input()
            try:
                self.username = JSONhandle(self.file_path).read_file(self.filename, 'Name')
                self.password = JSONhandle(self.file_path).read_file(self.filename, 'Password')
                correct_name = True
                RD.CommandShow(f"Your Username is: {self.username} and Password is: {Decryptor(self.password).decrypt_password()}").Info()
            except FileNotFoundError:
                RD.CommandShow("Password file not found.").Info()
            except:
                correct_name = False
                
    def del_login(self):
        correct_name = False
        while not correct_name:
            array = RD.CommandShow("Enter the name of the login you want to delete").Input()
            if not RD.Quest_result.lower() == 'exit':
                try:
                    JSONhandle(self.file_path).del_contents(array=array)
                    correct_name = True
                except KeyError: RD.CommandShow("Login not found. Please try again.").Info()
            else:
                correct_name = True
                

    def greet(self):
        RD.CommandShow("Welcome to the Makro Password Manager\nWhat would you like to do?").Choice(Button1='Delete Login', Button2='View Login', Button3='New Login')
        RD.Quest_result = RD.Quest_result.lower().strip(' ')
        if RD.Quest_result.lower().strip(' ') == 'new login':
            self.add_password()
        elif RD.Quest_result.lower().strip(' ') == 'view login':
            self.view_passwords()
        elif RD.Quest_result.lower().strip(' ') == 'delete login':
            self.del_login()
            

        
if __name__ == "__main__":
    passwd = PasswordManager()
    passwd.greet()