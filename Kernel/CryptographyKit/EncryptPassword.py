"""PyTerminal Cryptography Library"""
from Kernel.CryptographyKit.utils import _d_encrypt, edit_json
import base64

def encrypt_password(password, save=True):
    # Encrypt the password using a key
    encrypted_password = base64.b64encode(_d_encrypt(type='1', input_text=password).encode()).decode()
    if save:
        edit_json(loc1='user_credentials', loc2='Password', content=encrypted_password)
    return encrypted_password