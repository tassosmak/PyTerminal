from random import shuffle, choice
from Kernel import flags
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