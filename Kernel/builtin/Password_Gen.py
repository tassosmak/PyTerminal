from random import shuffle, choice
import string

def gen():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    length = int(input("How long do you want your password to be:"))
    shuffle(characters)
    password = []
    for i in range(length):
        password.append(choice(characters))
    password_str = ''.join(str(e) for e in password)
    print("".join(password))
    save_ask = input("Would You like to export the password to a txt?\n if YES press y")
    if save_ask == "y" or save_ask == "Y":
        f = open("password.txt", "w")
        f.write(password_str)
        print('The File Is Saved')

gen()