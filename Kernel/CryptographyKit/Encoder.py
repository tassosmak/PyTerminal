def liststr(l: list):
  string = ""
  for i in l:
    string += str(i)

  return string

def toBinary(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def binarystring(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def encode(string):
  encoded = toBinary(string)
  encoded = encoded.replace('00','erydta').replace("01","uicnajdja").replace("10","afsuid").replace("11","iajcjdhcnaberyr")
  return encoded

def decode(string: str):
  decoded = string.replace('erydta','00').replace("uicnajdja","01").replace("afsuid","10").replace("iajcjdhcnaberyr","11")
  return binarystring(decoded)
