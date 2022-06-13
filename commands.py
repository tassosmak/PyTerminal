import imp
import os
import datetime
import sys
from pathlib import Path

dir = Path(__file__).parent.resolve()

CML =[
"test",
"about",
"ABOUT",
"time",
"exit"

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
"exit"

]
MD = 0


def CommandList():
    global LCommand
    Command = input()
    LCommand = 0

    if Command == "LS":
        if MD == "2":
            print(os.listdir(dir))
        else:
            print("This Function isn't available within this mode")

    if Command == "test":
        LCommand = Command
        print("tested")
    
    if Command == "about" or Command == "ABOUT":
        LCommand = Command
        print("PyTerminal By Tassos Mak")
    
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
        if MD == "2":
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
                ask_del_create = input("This file already exist")
        elif MD == "2":
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



    if Command == "Exit":
        if MD == "1":
            ask_exit = input("Are you sure. if yes press 'Y' and hit return")
            if ask_exit == "Y":
                sys.exit()
        elif MD == "2":
            sys.exit()

        
