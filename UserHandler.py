from pathlib import Path
import datetime
import commands
import platform
import Kernel
import csv
import os
from src import FTU_Installer as ftu_install, settings

cmd = commands
csv = csv
kernel = Kernel


base_folder = Path(__file__).parent.resolve()
data_file = base_folder/"UserList.csv"





'''
UserLogin Handler

'''


pl = 0
UserMD = 0



def _create_csv_file(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Name/Mode")
        writer.writerow(header)

def _add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def _add_csv_data_ov(data_file, data):
    with open(data_file, 'w') as f:
        header = ("Name/Mode")
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

def _add_csv_data_headless(data_file, data):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def _find_index(input):
    global UserMD, row
    fl = open('UserList.csv', 'r').readlines()
    for row in fl:
        if row.find(input):
                UserMD = row



def ask():
    global username_ask, UserMD
    username_ask = input("Enter Usename")
    UserSearch = open(data_file, "r")
    if(username_ask in UserSearch.read()):
        _find_index(username_ask)
        for i in row:
            if int(i.isnumeric()):
                UserMD = i
                settings.MODE = i
                UserSearch.close()
        if username_ask == "":
            cmd.CommandSay("Not Typing A Name isn't allowed\nThus You Have Entered Safe-Mode", "FAIL")
            settings.MODE = "3"
            
    else:
        NewUser = input("This Username Doesn't exist do you want to create a user with this name")
        if NewUser == "Y" or NewUser == "y":
            ask_UserMD = input("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode\nChoose One!")
            data = (username_ask, ask_UserMD)
            _add_csv_data(data_file, data)
            UserMD = ask_UserMD


def Change_Listed_MODE(NEW_MODE):
    data = (username_ask, NEW_MODE)
    _add_csv_data_ov(data_file=data_file, data=data)



'''

WorkSpaceHandler

still in dev

'''

FirstTimeUse = 0
ask_type = 0
init_file = base_folder/"FTU.csv"
row = 0
Use = 0

def init():
    check_0 = open(init_file, "r")
    if("0" in check_0.read()):
        #cmd.CommandSay(answer="Welcome To PyTerminal By Tassos Makrostergios\nDon't Wory it an one time only message ;)\n")
        _FTS()
        check_0.close()
    check = open(init_file, "r").readline()
    for i in check:
        if check.isnumeric():
            if check == "2":
                settings.server_use = True
            Use = check
    with open('src/history.log', 'a') as f:    
        now = datetime.datetime.now()
        f.write(now.strftime("%Y-%m-%d %H:%M\n"))
            

def _FTS():
    cmd.CommandSay(answer="Welcome To PyTerminal By Tassos Makrostergios\nDon't Worry it's an one time only message ;)\n")
    FirstTimeUse = open("FTU.csv", "a")       
    ask_type = input("\n\nHow Do You want to use this instanche?\nPersonal Or Server")
    if ask_type == "1":
        ask_type = "1"
        data = ask_type
        _add_csv_data_headless(init_file, data)
    elif ask_type == "2":
        ask_type = "2"
        data = ask_type
        _add_csv_data_headless(init_file, data)
    else:
        cmd.CommandSay(answer="Fail FTS", color="FAIL")
    ftu_install.install(name="pyrad")
    ftu_install.install(name="clipboard")
    try:
        import pyrad
        import clipboard
    except ModuleNotFoundError:
        cmd.CommandSay("PIP is missing\ncritical features will not work", "FAIL")
    if not settings.MODE == "9":
        if settings.pl == "1" or settings.pl == "3":
            os.system("clear")
        elif settings.pl == "2":
            os.system("cls")
        




'''
Platform Identifier
'''


def pl_finder():
    global pl
    pl = platform.platform()

    if pl.startswith("macOS"):
        #os.system("killall python")
        pl = "1"
    elif pl.startswith("Windows"):
        pl = "2"
    elif pl.startswith("Linux"):
        #os.system("killall python")
        pl = "3"
    settings.pl = pl