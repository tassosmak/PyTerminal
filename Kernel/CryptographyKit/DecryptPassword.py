import json
import base64
from Kernel import flags
from Kernel.CryptographyKit.utils import _d_encrypt

def decrypt_password(password):
    
    
    # Decrypt the password using the key
    
    decrypted_password = base64.b64decode(password.encode()).decode()
    decrypted_password = _d_encrypt(type='2', input_text=decrypted_password)
    
    return decrypted_password

def ask_decrypt():
    try:
        f = open("MakroPropiatery.json")
        f.close()
    except FileNotFoundError:
        from RendererKit import Renderer as RD
        from os import _exit
        from Kernel.utils import edit_json
        RD.CommandSay(answer='You Dont Have the Privilages to Enter This Mode', color='FAIL')
        edit_json(loc1='Internal-Software', loc2='Enable', content='0')
        _exit(1)
    key = input("Enter key")
    password = input("\nEnter Password")
    decrypt_password(key, password)