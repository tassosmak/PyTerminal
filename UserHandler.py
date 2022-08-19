import importer as imp

cmd = imp.commands
csv = imp.csv
Path = imp.Path
kernel = imp.Kernel


base_folder = Path(__file__).parent.resolve()
data_file = base_folder/"UserList.csv"




'''
UserLogin Handler

'''



UserMD = 0



def create_csv_file(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Name/Mode")
        writer.writerow(header)

def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def find_index(input):
    global UserMD, row
    fl = open('UserList.csv', 'r').readlines()
    for row in fl:
        if row.find(input):
                #print(row)
                UserMD = row



def ask():
    global username_ask, UserMD
    username_ask = input("Enter Usename")
    UserSearch = open(data_file, "r")
    if(username_ask in UserSearch.read()):
        find_index(username_ask)
        for i in row:
            if int(i.isnumeric()):
                UserMD = i 
                #print(i)
        
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
            UserMD = ask_UserMD

# def Change_Listed_MODE(NEW_MODE):
#     ask_sure = input("Are you sure that you want to change the listed mode\nif yes press Y or y")
#     if ask_sure == "Y" or ask_sure == "y":
        


'''

WorkSpaceHandler

still in dev

'''
class WorkSpaceHandler(): 
    FirstTimeUse = 0
    ask_type = 0
    init_file = base_folder/"FTU.csv"
    row = 0
    Use = 0

    def init():
        check_0 = open(WorkSpaceHandler.init_file, "r")
        if("0" in check_0.read()):
            WorkSpaceHandler.FTS()
            check_0.close()
        check = open(WorkSpaceHandler.init_file, "r").readline()
        # print("before for")
        for i in check:
            # print("in for")
            if check.isnumeric():
                WorkSpaceHandler.Use = check
                cmd.ssh = True
                # print(WorkSpaceHandler.Use)
                # print("5")
                
                        



    def FTS():
        FirstTimeUse = open("FTU.csv", "a")       
        ask_type = input("How Do You want to use this instanche?\nPersonal Or Server")
        if ask_type == "1":
            ask_type = "1"
            print(ask_type)
            data = ask_type
            add_csv_data(WorkSpaceHandler.init_file, data)
        elif ask_type == "2":
            ask_type = "2"
            print(ask_type)
            data = ask_type
            add_csv_data(WorkSpaceHandler.init_file, data)
        else:
            print("Fail FTS")
    #     elif ask_type == "Server" or ask_type == "SERVER" or ask_type == "server":