import json
import base64

def decrypt_password(password):
    # Load the encrypted password and key from the file
    f = open("Info.json")
    data = json.load(f)
    Password = data['user_credentials']['Password']
    
    # Decrypt the password using the key
    decrypted_password = base64.b64decode(Password.encode()).decode()   
    f.close()        
    return decrypted_password

def ask_decrypt():
    try:
        f = open("MakroPropiatery.json")
        f.close()
    except FileNotFoundError:
        from RendererKit import Renderer as RD
        from os import _exit
        from UserHandlingKit.utils import edit_json
        RD.CommandSay(answer='You Dont Have the Privilages to Enter This Mode', color='FAIL')
        edit_json(loc1='Internal-Software', loc2='Enable', content='0')
        _exit(1)
    key = input("Enter key")
    password = input("\nEnter Password")
    decrypt_password(key, password)