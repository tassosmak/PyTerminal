import json
import base64
from RendererKit import Renderer as RD
from os import _exit

def decrypt_password(key, password):
    # Load the encrypted password and key from the file
    try:
        f = open("MakroPropiatery.json")
        data = json.load(f)
        Password = data['user_credentials']['Password']
        key_json = data['user_credentials']['Key']
    except FileNotFoundError:
        RD.CommandSay(answer='You Dont Have the Privilages to Enter This Mode')
        _exit(1)
    while key != key_json:
        key = input("Enter key: ")
    
    
    # Decrypt the password using the key
    decrypted_password = base64.b64decode(Password.encode()).decode()
 
    while password != decrypted_password:
        password = input("Enter Password: ")
            
    return decrypted_password

def ask_decrypt():
    key = input("Enter key")
    password = input("\nEnter Password")
    decrypt_password(key, password)