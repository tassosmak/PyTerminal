from random import shuffle, choice
from Makro.MakroCore import flags
from Makro.MakroCore.JSONhander import JSONhandle
import string
import json


#Start - Legacy Scraped
def _reverse_key(text=''):
    str = ""
    for i in text:
        str = i + str
    return str


def _d_encrypt(type=0, input_text='', save=True):
    outstr = "abcdenghik"
    instr = "1234567890"

    if type == "1":
        trans = str.maketrans(instr, outstr)
        final_text = input_text.translate(trans)
        Dresult = _reverse_key(final_text)
        if save:
            edit_json(loc1='user_credentials', loc2='Password', content=Dresult)
    elif type == '2':
        reverse = str.maketrans(outstr, instr)
        final_text = input_text.translate(reverse)
        Dresult = _reverse_key(final_text)
    return Dresult
#End - Legacy Scraped


def edit_user_config(username=str, Loc1=str, Loc2=str, Content=str):
    """Edit User Config File"""
    try: 
        f = open(f'{flags.base_folder}/users/{username}.json', 'r')
        f.close()
    except FileNotFoundError:
        open(f'{flags.base_folder}/users/{username}.json', 'w+').close()
        from Makro.MakroCore.src import Recover_Json
        Recover_Json.gen_file(username)
    JSONhandle(f'{flags.base_folder}/users/{username}.json').edit_json(
        loc1=Loc1,
        loc2=Loc2,
        content=Content 
        )



def edit_json(file_name='Info.json', loc1="", loc2="", content=""):
    with open(file_name, 'r+') as f:
        data = json.load(f)
        if not loc2 == "":
            data[loc1][loc2] = content
        else:
            data[loc1] = content
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def _gen_safe_password(length=8):
    global final_password
    characters = list(string.digits)
    shuffle(characters)
    password = []
    for i in range(length):
        password.append(choice(characters))
    password_str = ''.join(str(e) for e in password)
    final_password = str(password_str)
    # if save:
        # _d_encrypt(type='1', input_text=final_password)
    return final_password


#NT --> New Technology | Start
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


def _encode(string):
  encoded = toBinary(string)
  encoded = encoded.replace('00','erydta').replace("01","uicnajdja").replace("10","afsuid").replace("11","iajcjdhcnaberyr")
  return encoded
#NT --> New Technology | End