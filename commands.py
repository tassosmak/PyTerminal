import os
import datetime
import sys
import clipboard
from pathlib import Path

'''
Adding Modules From Different Folders
'''
sys.path.insert(0,'PyTerminal/src')
from src import Server
from src import client
from src import Password_Gen as pswd_gen





dir = Path(__file__).parent.resolve()

CML =[
"test",
"about",
"ABOUT",
"time",
"exit",
"Version"

]


CMLAD =[
"LS",
"test",
"about",
"ABOUT",
"CML",
"time",
"delete",
"del",
"exit",
"Vesion",
"create",

]
MD = 0
Version = 2
jump = False


def CommandAsk(Admin=False):
    CommandList(Command=input()) 

def CommandList(Command=0):
    global jump
    global LCommand
    LCommand = 0

    if Command == "LS":
        if MD == "2":
            print(os.listdir(dir))
        else:
            print("This Function isn't available within this mode")

    if Command == "test":
        LCommand = Command
        print("tested")
    
    if Command == "about" or Command == "ABOUT" or Command == "Version" or Command == "version": 
        LCommand = Command
        print(f"PyTerminal V.Alpha by Tassos Mak")
    
    if Command == "CML":
        if MD == "2":
            print(CMLAD)
        elif MD == "1":
            LCommand = Command
            print(CML)
        else:
            print("This Function isn't available within this mode")
    
    if Command == "time":
        LCommand = Command
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"))

    if Command == "del" or Command == "delete":
        if MD == "2" or MD == "999":
            print(os.listdir(dir))
            ask_del = input("what file you want to delete:")
            try:
                print(ask_del)
                os.remove(ask_del)
                print("DONE")
            except FileNotFoundError:
                print("This file doesn't exist")
        else:
            print("This Function isn't available within this mode")

    if Command == "create":
        if MD == "1":
            LCommand = Command
            ask_name = input("What the name of the file you want to create?")
            try:
                open(ask_name, "x")
                print("DONE")
            except FileExistsError:
                ask_del_create = input("This file already exist try again")
            except UnboundLocalError:
                print("There was a Problem try again")
        elif MD == "2" or MD == "999":
                ask_name = input("What the name of the file you want to create?")
                try:
                    open(ask_name, "x")
                    print("DONE")
                except FileExistsError:
                    ask_del_create = input("This file already exist do you want to delete it. if yes type 'Y'")
                if ask_del_create == "Y" or ask_del_create == "y":
                    os.remove(ask_name)
                    print("DONE")
        else:
            print("This Function isn't available within this mode")

    if Command == "latest":
        clipboard.copy(open("history.log", mode= "r"))
        print("DONE")

    if Command == "gen password":
        pswd_gen.gen(MODE = MD)


    if Command == "Exit":
        if MD == "1":
            ask_exit = input("Are you sure. if yes press 'Y' and hit return")
            if ask_exit == "Y":
                sys.exit()
        elif MD == "2" or MD == "999":
            sys.exit()

        
    if Command == "jump":
        LCommand = Command
        jump = True
    
    if Command == "print md":
        if MD == "2" or MD == "999":
            print(MD)
        else:
            print("This Function isn't available within this mode\nif you need to use this\ni suggest that you use the 'jump' command")



    if Command == "COM":
        ask_type = input("do you want to be host or reciever\nif you want to be host press 1 otherwise prees 2")
        if ask_type == "1":
            Server.chat()
        else:
            client.Chat()