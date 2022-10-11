import sys
 
# setting path
sys.path.append('../PyTerminal')
 
import string
from random import random, shuffle, choice
import settings

MODE = settings.MODE
def gen():
    
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    length = int(input("How long do you want your password to be:"))
    shuffle(characters)
    password = []
    for i in range(length):
        password.append(choice(characters))
    password_str = ''.join(str(e) for e in password)
    print("".join(password))
    #print("\033[1;32m \n".join(password))
    if MODE == "2" or MODE == "9":
        save_ask = input("Would You like to export the password to a txt?\n if YES press y")
        if save_ask == "y" or save_ask == "Y":
            f = open("export.log", "w")
            f.write(password_str)
            print('DONE')
        else:
            print("DONE")
            pass


gen()
sys.exit()