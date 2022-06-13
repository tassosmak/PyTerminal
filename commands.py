import os
import datetime
from pathlib import Path



dir = Path(__file__).parent.resolve()

CML =[
"test",
"about",
"ABOUT",
"time",

]


CMLAD =[
"LS",
"test",
"about",
"ABOUT",
"CML",
"time",
"delete",
"del"

]
MD = 0


def CommandList():
    global LCommand
    Command = input()
    LCommand = 0

    if Command == "LS":
        if MD == "2":
            LCommand = Command
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
            LCommand = Command
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
                os.remove(ask_del)
                print("OK")
            except FileNotFoundError:
                print("This file doesn't exist")
        else:
            print("This Function isn't available within this mode")

    # if Command == "Kill":
    #     return

        
