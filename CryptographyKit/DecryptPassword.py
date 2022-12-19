import json
import base64

def decrypt_password(key, password):
    # Load the encrypted password and key from the file
    f = open('MakroPropiatery.json')
    data = json.load(f)
    Password = data['user_credentials']['Password']
    key_json = data['user_credentials']['Key']

    while key != key_json:
        key = input("Enter key: ")
    
    
    # Decrypt the password using the key
    decrypted_password = base64.b64decode(Password.encode()).decode()

    while password != decrypted_password:
        password = input("Enter Password: ")
            
    return decrypted_password

def ask_decrypt():
    key = input("Enter key: ")
    password = input("Enter Password: ")
    decrypt_password(key, password)

if __name__ == "__main__":
    ask_decrypt()
