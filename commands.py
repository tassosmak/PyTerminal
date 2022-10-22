try:
    DNT_IMP_clipboard = False
    import os
    import datetime
    import platform
    import sys
    import Boot
    from pathlib import Path

    net = False
    try:
        import clipboard
    except ModuleNotFoundError:
        DNT_IMP_clipboard = True
        pass
    '''
    Adding Modules From Different Folders
    '''
    try:
        from src import Server
        from src import client
        net = True
    except OSError:
        print("\nunfortunately due to many instanches running at the same time it's not possible to connect to the network\nso the browsing expirience is unavailable\n")
        net = False



    dir = Path(__file__).parent.resolve()

    CML =[
    "test",
    "about",
    "ABOUT",
    "time",
    "exit",
    "Version",
    "jump",
    "jump_user"

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
    plt = 0
    USNAME_PRINT = 0
    sys_detect = platform.uname()
    MD = 0
    Version = 2
    jump = False
    jump_user = False
    ask_recv = 0
    answer = 0
    ssh = False

    def CommandAsk(Admin=False, plt=0, USNAME_PRINT=0):
        if MD == "2":
            CommandList(Command=input(f"!History isn't enabled! PyTerminal Beta | {USNAME_PRINT.capitalize()} % "), cmd_pl=plt)
        elif MD == "9": 
            CommandList(Command=input(f"PyTerminal {sys_detect.processor} | {sys_detect.system} {sys_detect.machine} % "), cmd_pl=plt)
        else:
            CommandList(Command=input(f"PyTerminal Beta | {USNAME_PRINT.capitalize()} $ "), cmd_pl=plt) 


    def CommandList(Command=0, cmd_pl=0):
        global jump, jump_user, ask_recv, LCommand, answer
        LCommand = 0

        if Command == "ls":
            if MD == "2":
                CommandSay(answer=os.listdir(dir))
            else:
                CommandSay(answer="This Function isn't available within this mode", color="WARNING")

        if Command == "test":
            LCommand = Command
            if MD == "9":
                CommandSay(answer="tested")
                CommandSay(answer="tested", color="WARNING")
                CommandSay(answer="tested", color="FALI")
                CommandSay(answer="tested", color="OKGREEN")
                if cmd_pl == "1":
                    now = datetime.datetime.now()
                    CommandPush(message=f'Tested {now.strftime("%Y-%m-%d %H:%M:%S")}')
                if not cmd_pl == "3":
                    Boot.Run = True
                    Boot.SecondaryTask("test", stay_end=True)
            else:
                CommandSay(answer="tested")
        
        if Command == "about" or Command == "ABOUT" or Command == "Version" or Command == "version": 
            LCommand = Command
            CommandSay(answer="PyTerminal V.Alpha by Tassos Mak")
        
        if Command == "CML":
            if MD == "2":
                CommandSay(answer=CMLAD)
            elif MD == "1":
                LCommand = Command
                CommandSay(answer=CML)
            else:
                CommandSay(answer="This Function isn't available within this mode", color="WARNING")
        
        if Command == "time":
            LCommand = Command
            now = datetime.datetime.now()
            CommandSay(answer=now.strftime("%Y-%m-%d %H:%M:%S"))

        if Command == "del" or Command == "delete":
            
            if MD == "2":
                CommandSay(answer=os.listdir(dir))
                ask_del = input("what file you want to delete:")
                try:
                    CommandSay(answer=ask_del)
                    os.remove(ask_del)
                    CommandSay(answer="DONE", color="OKGREEN")
                except FileNotFoundError:
                    CommandSay(answer="This file doesn't exist", color="FAIL")
            else:
                LCommand = Command
                CommandSay(answer="This Function isn't available within this mode", color="FAIL")

        if Command == "create":
            if MD == "1":
                LCommand = Command
                ask_name = input("What the name of the file you want to create?")
                try:
                    open(ask_name, "x")
                    CommandSay(answer="DONE", color="OKGREEN")
                except FileExistsError:
                    ask_del_create = input("This file already exist try again", color="WARNING")
                except UnboundLocalError:
                    CommandSay(answer="There was a Problem try again", color="FAIL")
            elif MD == "2" or MD == "9":
                    ask_name = input("What the name of the file you want to create?")
                    try:
                        open(ask_name, "x")
                        CommandSay(answer="DONE", color="OKGREEN")
                    except FileExistsError:
                        ask_del_create = input("This file already exist do you want to delete it. if yes type 'Y'")
                        if ask_del_create == "Y" or ask_del_create == "y":
                            os.remove(ask_name)
                            CommandSay(answer="DONE", color="OKGREEN")
                    except UnboundLocalError:
                            pass
            else:
                CommandSay(answer="This Function isn't available within this mode", color="FALI")

        if Command == "latest":
            LCommand = Command
            if DNT_IMP_clipboard:
                CommandSay(answer="To use this command you have to install the clipboard module", color="FAIL")
                
            else:
                clipboard.copy(open("history.log", mode= "r"))
                print("DONE")

        if Command == "gen password":
            Boot.Run = True
            Boot.SecondaryTask(file_name="Password_Gen", stay_end=True)


        if Command == "Exit":
            if MD == "1":
                ask_exit = input("Are you sure. if yes press 'Y' and hit return")
                if ask_exit == "Y" or ask_exit == "y":
                    sys.exit()
            elif MD == "2" or MD == "9":
                sys.exit()

            
        if Command == "jump":
            LCommand = Command
            jump = True

        if Command == "jump user":
            LCommand = Command
            jump_user = True


        if Command == "print md":
            if MD == "2":
                CommandSay(answer=MD)
            else:
                LCommand = Command
                CommandSay(answer="This Function isn't available within this mode\nif you need to use this\ni suggest that you use the 'jump' command", color="WARNING") 


        
        if Command == "talk":
            LCommand = Command
            if net:
                ask_type = input("do you want to be host or reciever\nif you want to be host press 1 otherwise prees 2")
                if ask_type == "1":
                    Server.chat()
                else:
                    ask_recv = input("To Which IP you want to talk to\nType Below!\n:")
                    CommandSay(answer=ask_recv)
                    try: 
                        client.Chat(IP=ask_recv)
                    except ConnectionRefusedError:
                        CommandSay(answer="This User is Unavilable at the moment\ntry again later", color="WARNING")
            else:
                CommandSay(answer="You Are in Safe Mode you can't connect to the internet right now")



        if Command == "clear":
            if cmd_pl == "1" or cmd_pl == "3":
                os.system('clear')
            else:
                os.system('cls')

        if Command == "view file":
            LCommand = Command
            ask_file = input("type the name of the file you want to view\n:")
            if cmd_pl == "1" or cmd_pl == "3":
                os.system(f"open {ask_file}")
            elif cmd_pl == "2":
                os.system(f"more {ask_file}")
        
        if Command == "edit file":
            if MD == "2":
                LCommand = Command
                if cmd_pl == "1" or cmd_pl == "3":
                    ask_file = input("type the name of the file you want to edit\n:")
                    if ask_file.endswith(".py"):
                        os.system(f"vim {ask_file}")
                    else:
                        os.system(f"nano {ask_file}")
                elif cmd_pl == "2":
                    CommandSay(answer="You can't edit files within The Windows Command Prompt", color="FAIL")
            else:
                CommandSay(answer="This Function isn't available within this mode", color="FALI")
        
        if Command == "weather forecast":
            LCommand = Command
            if net:
                weather = os.system("curl wttr.in/")
                CommandSay(answer="This is a fork from @igor_chubin", color="UNDERLINE") 
            else:
                CommandSay(answer="You Are in Safe Mode so you can't connect to the internet right now")

        if Command == "activity monitor":
            if MD == "2":
                if cmd_pl == "1" or cmd_pl == "3":
                    LCommand = Command
                    os.system('top')
            else:
                CommandSay(answer="This Function isn't available within this mode", color="FALI")

        if Command == "countdown":
            LCommand = Command
            Boot.Run = True
            Boot.SecondaryTask(file_name="countdown", stay_end=False)
            
            
        
        if Command == "check site status":
            if MD == "2" or MD == "9":
                LCommand = Command
                site = input("type the site you want to check:\n")
                os.system(f"ping {site}")
                
            else:
                CommandSay(answer="This Function isn't available within this mode", color="FALI")
        

    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        WHITE  = '\33[37m'

    def CommandPush(message):
        command = f'''
        osascript -e 'display notification "{message}" with title "PyTerminal"'
        '''
        os.system(command)



    def CommandSay(answer=0, color=0):
        # if ssh == True:
        #     if color == "WARNING":
        #         print("\n",bcolors.WARNING, answer, f"{bcolors.WHITE} ") and Server.SendOnly(Say=answer)
        #     elif color == "FAIL":
        #         print("\n",bcolors.FAIL, answer, f"{bcolors.WHITE} ") and Server.SendOnly(Say=answer)
        #     elif color == "OKGREEN":
        #         print("\n",bcolors.OKGREEN, answer, f"{bcolors.WHITE} ") and Server.SendOnly(Say=answer)
        #     else:
        #         print("\n",answer) and Server.SendOnly(Say=answer)
        # else:
        if color == "WARNING":
            print("\n",bcolors.WARNING, answer, f"{bcolors.WHITE} ")
        elif color == "FAIL":
            print("\n",bcolors.FAIL, answer, f"{bcolors.WHITE} ")
        elif color == "OKGREEN":
            print("\n",bcolors.OKGREEN, answer, f"{bcolors.WHITE} ")       
        else:
            print("\n",answer)
            #print(answer)
except BaseException:
    import Error_Logger.Logger as logger
    logger.log_error(message="Command.py")
