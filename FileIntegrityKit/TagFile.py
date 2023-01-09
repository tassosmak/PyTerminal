from CryptographyKit import DecryptPassword

def read_enc(file_to_check=''):
    if not file_to_check == '':
        with open(file_to_check, 'r+') as file: 
            file.seek(0, 0)
            file_data = file.readline()
            decrypt_data = DecryptPassword.decrypt_password(password=file_data)
            return decrypt_data