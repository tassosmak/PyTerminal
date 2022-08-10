import commands
import csv
from pathlib import Path
cmd = commands


base_folder = Path(__file__).parent.resolve()
data_file = base_folder/"UserList.csv"


def create_csv_file(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Name", "Mode")
        writer.writerow(header)

def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def search_csv_data(input=0):
    global UserSearch
    UserSearch = open("UserList.csv", "r")



# data = ()
# add_csv_data(data_file, data)




def ask():
    global username_ask
    username_ask = input("Enter Usename")
    search_csv_data("username_ask")
    #print("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
    #ask_core = input("select Mode")
    if(username_ask in UserSearch.read()):
        print("ok")
    
    


    



    else:
        NewUser = input("This Username Doesn't exist do you want to create a user with this name")
        if NewUser == "Y" or NewUser == "y":
            '''
            ask phase
            '''
            ask_UserMD = input("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode\nChoose One!")
            

            '''
            append phase
            '''       
            data = (username_ask, ask_UserMD)
            add_csv_data(data_file, data)
ask()






# #cmd.MD = ask_core
# print("Go Ahead")




























