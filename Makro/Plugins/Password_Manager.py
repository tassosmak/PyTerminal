import json, os

from src.utils import add_depend, sys
add_depend(str(sys.argv[1]))

from Makro.MakroCore.CryptographyKit import EncryptPassword as EP
from Makro.MakroCore.CryptographyKit.decrypt import Decryptor
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags

class PasswordManager:
    
    def __init__(self):
        self.file_path = f'{flags.base_folder}/../Plugins/src/pwdfile.json'
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


    def read_file(self, pwd_name, print_credentials=False):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as recover:
                try:
                    data = json.load(recover)
                    if flags.EnableIntSoft:
                        RD.CommandShow(msg=f"Reading file contents: {data}").Show('BLUE')
                except json.JSONDecodeError:
                    RD.CommandShow("Error reading password file").Info()
        else:
            RD.CommandShow("No password file found.").Info()
            return self.add_password()

        _username = data[pwd_name]['Name']
        _password = data[pwd_name]['Password']
        
        if flags.EnableIntSoft:
            if print_credentials:
                RD.CommandShow(msg=("Username:", _username)).Show('BLUE')
            
            if print_credentials:
                RD.CommandShow(msg=("Password:", _password)).Show('BLUE')
                
        return _username, _password



                                                                                                                                                                                         
    def add_password(self):
        self.filename = RD.CommandShow('Give a name to the file where you want to save your passwords').Input()
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
                self.username, self.password = self.read_file(self.filename)
                correct_name = True
                RD.CommandShow(f"Your Username is: {self.username} and Password is: {Decryptor(self.password).decrypt_password()}").Info()
            except FileNotFoundError:
                RD.CommandShow("Password file not found.").Info()
    


    def greet(self):
        RD.CommandShow("Welcome to the Makro Password Manager!\nWhat would you like to do?").Choice(Button1='Add Password', Button2='View Passwords')
        RD.Quest_result = RD.Quest_result.lower().strip(' ')
        if RD.Quest_result.lower().strip(' ') == 'add password':
            self.add_password()
        elif RD.Quest_result.lower().strip(' ') == 'view passwords':
            self.view_passwords()

        
if __name__ == "__main__":
    passwd = PasswordManager()
    passwd.greet()