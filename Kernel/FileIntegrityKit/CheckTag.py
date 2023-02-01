from UserHandlingKit.utils import _gen_safe_password
from CryptographyKit import EncryptPassword

def write_enc():
    line = _gen_safe_password(length=14)
    print(line, '2')
    enc_line = EncryptPassword.encrypt_password(line, save=False)

    with open('src/settings.py', 'r+') as file: 
        file_data = file.read() 
        file.seek(0, 0)
        file.write('#' + enc_line + '\n' + file_data)