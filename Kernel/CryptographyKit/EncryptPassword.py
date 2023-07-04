"""PyTerminal Cryptography Library"""
from Kernel.CryptographyKit.utils import edit_json
from Kernel.CryptographyKit.Encoder import encode

def encrypt_password(password, save=True):
    # Encrypt the password using a key
    encrypted_password = encode(password)
    if save:
        edit_json(loc1='user_credentials', loc2='Password', content=encrypted_password)
    return encrypted_password