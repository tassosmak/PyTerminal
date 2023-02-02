import json
import base64
from Kernel.utils import _d_encrypt




def edit_json(file_name='Info.json', loc1="", loc2="", content=""):
    with open(file_name, 'r+') as f:
        data = json.load(f)
        if not loc2 == "":
            data[loc1][loc2] = content
        else:
            data[loc1] = content
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def encrypt_password(password, save=True):
    # Encrypt the password using a key
    # encrypted_password = 
    encrypted_password = base64.b64encode(_d_encrypt(type='1', input_text=password).encode()).decode()
    if save:
        edit_json(loc1='user_credentials', loc2='Password', content=encrypted_password)
    return encrypted_password



def main():
    # Read the password and key from the user
    password = input("Enter password: ")
    key = input("Enter key: ")

    # Encrypt the password and save it to the file
    encrypt_password(password, key)