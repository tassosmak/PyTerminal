"""PyTerminal Cryptography Library"""
from Makro.MakroCore.CryptographyKit.utils import edit_user_config, _encode
from Makro.MakroCore import flags




def encrypt_password(password, save=True):
    # Encrypt the password using a key
  encrypted_password = _encode(password)
  if save:
      edit_user_config(
          username=flags.USERNAME,
          Loc1='user_credentials',
          Loc2='Password',
          Content=encrypted_password)

  return encrypted_password