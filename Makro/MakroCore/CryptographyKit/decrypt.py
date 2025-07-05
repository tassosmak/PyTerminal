class Decryptor:
    '''PyTerminal Decryption Library'''    
    def __init__(self, password: str):
        self.password = password
    
    def binarystring(bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

    def _decode(string: str):
        decoded = string.replace('erydta','00').replace("uicnajdja","01").replace("afsuid","10").replace("iajcjdhcnaberyr","11")
        return Decryptor.binarystring(decoded)

    def decrypt_password(self):
        decrypted_password = Decryptor._decode(str(self.password))
        return decrypted_password


if __name__ == "__main__":
    print(Decryptor(input('Welcome to the PyTerminal Decryption Library\nEnter The Encrypted String:')).decrypt_password())