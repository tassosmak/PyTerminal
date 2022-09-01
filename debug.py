from pathlib import Path


base_folder = Path(__file__).parent.resolve()
data_file = base_folder/"UserList.csv"


username_found = False
mode_found = False



def find_index(input):
    global UserMD, row
    fl = open('UserList.csv', 'r').readlines()
    for row in fl:
        if row.find(input):
                UserMD = row

def check_num(num=0, match=0):
    if num == match:
        mode_found = True


class UserList():

    check_username_ask = input("Enter Usename")
    check_mode_ask = input("Enter Mode")


    username = check_username_ask
    mode = check_mode_ask


    UserSearch = open(data_file, "r")
    if(username in UserSearch.read()):
        username_found = True
        find_index(username)
        for i in row:
            if int(i.isnumeric()):
                check_num(num=i, match=mode)
        UserSearch.close()
    if username_found == True and mode_found == True:
        print("UserList.csv is okay")
    elif username_found == True and mode_found == False:
        print("username was found but we had a problem with the mode we couldnt find it")
    elif username_found == False and mode_found == True:
        print("mode was found but we had a problem with the username we couldnt find it")
    elif username_found == False and mode_found == False:
        print("we couldn't find anything regarding the information you gave us")
    else:
        print("UserList class FAIL")

        