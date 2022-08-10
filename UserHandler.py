import commands
cmd = commands


def ask():
    global username_ask
    username_ask = input("Enter Usename")
    #print("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode")
    #ask_core = input("select Mode")
    UserSearch = open("UserList.log", "r")
    if(username_ask in UserSearch.read()):
        print("ok")
    
    
    
    
    
    
    
    
    
    
    
    
    else:
        NewUser = input("This Username Doesn't exist do you want to create a user with this name")
        if NewUser == "Y" or NewUser == "y":
            '''
            init phase
            '''
            UserSearch = open("UserList.log", "a")
            UserMD = open("UserListMD.log", "a")
            
            '''
            ask phase
            '''
            ask_UserMD = input("there are 2 Modes on this terminal:\n1) The Basic Mode,     2) The Advanced Mode\nChoose One!")
            
            

            '''
            append phase
            '''
            UserSearch.write(str(f"{username_ask}{ask_UserMD}\n"))
            
            UserMD.write(str(f"{ask_UserMD}\n"))
ask()






#cmd.MD = ask_core
print("Go Ahead")


