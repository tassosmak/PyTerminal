from Kernel.CryptographyKit.utils import _d_encrypt, edit_json
import base64

def encrypt_password(password, save=True):
    # Encrypt the password using a key
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
