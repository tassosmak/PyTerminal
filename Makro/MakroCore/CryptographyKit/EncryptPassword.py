"""PyTerminal Cryptography Library"""
from Makro.MakroCore.CryptographyKit.utils import edit_json, toBinary

def _encode(string):
  encoded = toBinary(string)
  encoded = encoded.replace('00','erydta').replace("01","uicnajdja").replace("10","afsuid").replace("11","iajcjdhcnaberyr")
  return encoded


def encrypt_password(password, save=True):
    # Encrypt the password using a key
    encrypted_password = _encode(password)
    if save:
        edit_json(loc1='user_credentials', loc2='Password', content=encrypted_password)
    return encrypted_password