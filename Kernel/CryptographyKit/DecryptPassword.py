from Kernel.CryptographyKit.utils import _d_encrypt
import base64

def decrypt_password(password):
    decrypted_password = base64.b64decode(password.encode()).decode()
    decrypted_password = _d_encrypt(type='2', input_text=decrypted_password)
    return decrypted_password