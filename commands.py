try:
    DNT_IMP_clipboard = False
    import os
    import datetime
    import platform
    import Boot
    from pathlib import Path
    from UserHandlingKit.utils import edit_json
    from RendererKit import Renderer as RD
    from src import settings
    net = False

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
    
    
    file_list = [
        'commands.py',
        'Info.json',
        'Kernel.py',
        'launcer.py',
        'MakroPropiatery.py',
        'pyrad.log',
        'UserHandler.py',
        'Boot.py',
        'CryptographyKit/DecryptPassword.py',
        'CryptographyKit/EncryptPassword.py',
        'NetworkingKit/server.py',
        'NetworkingKit/auth.py',
        'RendererKit/Renderer.py',
        'RendererKit/WindowRenderer.py',
        'UserHandlingKit/credentials.py',
        'UserHandlingKit/FTU.py',
        'UserHandlingKit/utils.py',
        'UserHandlingKit/UserHandler.py'
    ]

    CML =[
    "test",
    "about",
    "ABOUT",
    "time",
    "exit",
    "version",
    "jump",
    "logout",
    "ls",
    "del",
    "print md",
    "countdown",
    "devices",
    "chatbox",
    "chatbox install",
    "activity monitor",
    "create",
    "edit file",
    "view file",
    "gen password",
    "latest",
    "edit parameters",
    "talk",
    "check site status",
    "weather forecast",
    ]
    
    plt = 0
    USNAME_PRINT = 0
    sys_detect = platform.uname()
    Version = 2
    jump = False
    logout = False
    jump_user = False
    ask_recv = 0
    answer = 0
    ssh = False

    def CommandAsk(plt=0, USNAME_PRINT=0, safe_mode=False, MD='0'):
        if MD == "2":
            CommandList(Command=input(f"!History isn't enabled! PyTerminal Beta | {USNAME_PRINT.capitalize()} % "), cmd_pl=plt, MD=MD)
        elif MD == "9": 
            CommandList(Command=input(f"PyTerminal {sys_detect.system} | {sys_detect.machine} % "), cmd_pl=plt, MD=MD)
        elif MD == "3":
            CommandList(Command=input(f"PyTerminal | Safe-Mode $ "), cmd_pl=plt, safe_md=safe_mode, MD=MD)
        else:
            CommandList(Command=input(f"PyTerminal Beta | {USNAME_PRINT.capitalize()} $ "), cmd_pl=plt, MD=MD) 


    def CommandList(Command=0, cmd_pl=0, safe_md=False, MD=0):
        global jump, logout, jump_user, ask_recv, LCommand, answer
        LCommand = 0

        if Command == "ls":
            if MD == "2":
                RD.CommandSay(answer=os.listdir(dir))
            else:
                RD.CommandSay(answer="This Function isn't available within this mode", color="WARNING")

        if Command == "test":
            LCommand = Command
            if MD == "9":
                RD.CommandSay(answer="tested")
                RD.CommandSay(answer="tested", color="WARNING")
                RD.CommandSay(answer="tested", color="FAIL")
                RD.CommandSay(answer="tested", color="OKGREEN")
                RD.CommandSay(answer="tested", color="PURPLE")
                RD.CommandSay(answer="tested", color="UNDERLINE")
                now = datetime.datetime.now()
                RD.CommandPush(message=f'Tested {now.strftime("%Y-%m-%d %H:%M:%S")}')
                RD.CommandQuest(type='2', msg=f'Tested {now.strftime("%Y-%m-%d %H:%M:%S")}')
                RD.CommandQuest(type='3', msg='Testing')
                RD.CommandSay(answer=RD.Quest_result, color="WARNING")
                RD.CommandQuest(type='1', msg="tested")
                if RD.Quest_result == 'Yes':
                    RD.CommandSay(answer='Positive answer', color='WARNING')
                else:
                    RD.CommandSay(answer='Negative answer', color='WARNING')
                if not cmd_pl == "3":
                    Boot.SecondaryTask(file_name="test", stay_end=True)
            else:
                RD.CommandSay(answer="tested")
        
        if Command == "about" or Command == "ABOUT" or Command == "Version" or Command == "version": 
            LCommand = Command
            RD.CommandSay(answer="PyTerminal V.Beta by Makro Software")
        
        if Command == "CML":
            LCommand == Command
            RD.CommandSay(answer=CML)
        
        if Command == "time":
            LCommand = Command
            now = datetime.datetime.now()
            RD.CommandSay(answer=now.strftime("%Y-%m-%d %H:%M:%S"))

        if Command == "del" or Command == "delete":
            if not safe_md:
                if MD == "2" or MD == '9':
                    RD.CommandSay(answer=os.listdir(dir))
                    ask_del = input("what file you want to delete:")
                    try:
                        RD.CommandSay(answer=ask_del)
                        os.remove(ask_del)
                        RD.CommandSay(answer="DONE", color="OKGREEN")
                    except FileNotFoundError:
                        RD.CommandQuest(type='2', msg="This file doesn't exist")
                else:
                    LCommand = Command
                    RD.CommandQuest(type='2', msg="This Function isn't available within this mode")

        if Command == "create":
            if not safe_md:
                if MD == "1":
                    LCommand = Command
                    RD.CommandQuest(type='3', msg="What the name of the file you want to create?")
                    try:
                        open(RD.Quest_result, "x")
                        RD.CommandSay(answer="DONE", color="OKGREEN")
                    except FileExistsError:
                        RD.CommandQuest(type='2', msg="This file already exist try again")
                    except UnboundLocalError:
                        RD.CommandQuest(type='2', msg="There was a Problem try again")
                elif MD == "2" or MD == "9":
                        RD.CommandQuest(type='3', msg="What the name of the file you want to create?")
                        try:
                            open(RD.Quest_result, "x")
                            RD.CommandSay(answer="DONE", color="OKGREEN")
                            ask_name = RD.Quest_result
                        except FileExistsError:
                            RD.CommandQuest(type='1', msg="This file already exist do you want to delete it. if yes type 'Y'", Button1='No', Button2='Yes')
                            if RD.Quest_result == "Yes" or RD.Quest_result == "yes":
                                os.remove(ask_name)
                                RD.CommandSay(answer="DONE", color="OKGREEN")
                        except UnboundLocalError:
                                pass
                else:
                    RD.CommandQuest(type='2', msg="This Function isn't available within this mode")

        if Command == "latest":
            Boot.SecondaryTask(file_name="LineRetriver")
            

        if Command == "gen password":
            if not safe_md:
                LCommand = Command
                Boot.SecondaryTask(file_name="Password_Gen", stay_end=True)


        if Command == "Exit" or Command == "exit":
            if MD == "1":
                LCommand = Command
                ask_exit = input("Are you sure. if yes press 'Y' and hit return")
                if ask_exit == "Y" or ask_exit == "y":
                    if cmd_pl == "1" or cmd_pl == "3":
                        os.system('killall python')
                    elif cmd_pl == "2":
                        os._exit(1)
            elif MD == "2" or MD == "9" or MD == "3":
                if cmd_pl == "1" or cmd_pl == "3":
                    os.system("killall python")
                elif cmd_pl == "2":
                    os._exit(1)

            
        if Command == "jump":
            if not safe_md:
                LCommand = Command
                jump = True


        if Command == "print md":
            if not safe_md:
                RD.CommandSay(answer=MD)
            else:
                RD.CommandSay("You Are in Safe-Mode", color='WARNING')



        if Command == "talk":
            if not safe_md:
                LCommand = Command
                if net:
                    RD.CommandQuest(type='1', ask_admin_msg='do you want to be host or reciever', Button1='Host', Button2='Talker')
                    #ask_type = input("do you want to be host or reciever\nif you want to be host press 1 otherwise prees 2")
                    if RD.Quest_result == "Host":
                        Server.chat()
                    elif RD.Quest_result == "Talker":
                        #ask_recv = input("To Which IP you want to talk to\nType Below!\n:")
                        RD.CommandQuest(type='3', msg='To Which IP you want to talk to Type Below!')
                        ask_recv = str(RD.Quest_result)
                        try: 
                            client.Chat(IP=ask_recv)
                        except ConnectionRefusedError:
                            if not RD.Quest_result == '':
                               RD.CommandSay(answer="This User is Unavilable at the moment\ntry again later", color="WARNING")
                            else:
                               pass 
                else:
                    RD.CommandSay(answer="You Are in Safe Mode you can't connect to the internet right now")



        if Command == "clear":
            if cmd_pl == "1" or cmd_pl == "3":
                os.system('clear')
            else:
                os.system('cls')

        if Command == "view file":
            LCommand = Command
            if settings.EnableIntSoft:
                Boot.SecondaryTask('view_file')
            else:
                RD.CommandQuest(type='3', msg='type the name of the file you want to view')
                #ask_file = input("type the name of the file you want to view\n:")
                if cmd_pl == "1" or cmd_pl == "3":
                    if not RD.Quest_result in file_list:
                        os.system(f"cat {RD.Quest_result}")
                elif cmd_pl == "2":
                    if not RD.Quest_result in file_list:
                        os.system(f"more {RD.Quest_result}")
        
        if Command == "edit file":
            if not safe_md:
                if MD == "2" or MD == '9':           
                    if cmd_pl == "1" or cmd_pl == "3":
                        RD.CommandQuest(type='3', msg='Type the name of the file you want to edit')
                        if not RD.Quest_result in file_list:
                            #ask_file = input("type the name of the file you want to edit\n:")
                            if RD.Quest_result.endswith(".py"):
                                os.system(f"vim {RD.Quest_result}")
                            else:
                                os.system(f"nano {RD.Quest_result}")
                    elif cmd_pl == "2":
                        RD.CommandQuest(type='3', msg='Type the name of the file you want to edit')
                        if not RD.Quest_result in file_list:
                            os.system(f'notepad {RD.Quest_result}')
                else:
                    LCommand = Command
                    RD.CommandSay(answer="This Function isn't available within this mode", color="FALI")
        
        if Command == "weather forecast":
            if not safe_md:
                LCommand = Command
                if net:
                    os.system("curl wttr.in/")
                    RD.CommandSay(answer="This is a fork from @igor_chubin", color="UNDERLINE") 
                else:
                    RD.CommandSay(answer="You Are in Safe Mode so you can't connect to the internet right now")

        if Command == "activity monitor":
            if not safe_md:
                if MD == "2" or MD == "9":
                    if cmd_pl == "1" or cmd_pl == "3":
                        Boot.SecondaryTask('top')
                else:
                    LCommand = Command
                    RD.CommandSay(answer="This Function isn't available within this mode", color="FALI")

        if Command == "countdown":
            if not safe_md:
                LCommand = Command
                Boot.SecondaryTask(file_name="countdown", stay_end=False)
                
            
        
        if Command == "check site status":
            if MD == "2" or MD == "9":
                site = input("type the site you want to check:\n")
                os.system(f"ping {site}")
                
            else:
                LCommand = Command
                RD.CommandSay(answer="This Function isn't available within this mode", color="FALI")


        if Command == "devices":
            if not safe_md:
                if not cmd_pl == "2":
                    if settings.FTU == "2":
                        import NetworkingKit.server
                    else:
                        import NetworkingKit.auth
                        if NetworkingKit.auth.DONE:
                            Boot.SecondaryTask(file_name="Handle-External-Devices", stay_end=True)
                else:
                    RD.CommandSay("LocalNetworking Isn't Supported On Windown Yet\nIt's Under Development :)")



        if Command == "logout":
            LCommand = Command
            logout = True
            if cmd_pl == "1" or cmd_pl == "3":
                os.system('clear')
            else:
                os.system('cls')
                
                
        if Command == "edit parameters":
            if MD == "9":
                ask_what_params = input('What parameters You Want to Edit\n1) GUI\n2) Use\nSelect:')
                if ask_what_params == '1':
                    ask_gui_params = input('Do You Want to Enable it or Disable it\nSelect')
                    if ask_gui_params == 'enable' or ask_gui_params == 'Enable':
                        edit_json(loc1='UI', loc2='Enable-AquaUI', content='1')
                        RD.CommandSay(answer='You Have to reboot to use the changes', color='WARNING')
                    elif ask_gui_params == 'disable' or ask_gui_params == 'Disable':
                        edit_json(loc1='UI', loc2='Enable-AquaUI', content='0')
                        RD.CommandSay(answer='You Have to reboot to use the changes', color='WARNING')
                elif ask_what_params == '2':
                    ask_use_params = input('How Do You Want To Use This Instanche?, Type "Server" or "Personal":')
                    if ask_use_params == "Server":
                        edit_json(loc1='FTU', loc2='Use', content='2')
                        RD.CommandSay(answer='You Have to reboot to use the changes', color='WARNING')
                    elif ask_use_params == 'Personal':
                        edit_json(loc1='FTU', loc2='Use', content='1')
                        RD.CommandSay(answer='You Have to reboot to use the changes', color='WARNING')


        if Command == 'chatbox':
            if not safe_md:
                if net:
                    Boot.SecondaryTask('chatgpt')
        if Command == 'chatbox install':
            if not safe_md:
                if net:
                    os.system('python3 src/chatgpt.py install')
                    if cmd_pl == "1" or cmd_pl == "3":
                        os.system('clear')
                    else:
                        os.system('cls')


        #DONT WRITE ANYTHING BELOW HERE
        else:
            if not Command in CML:
                if not Command == '' :
                    RD.CommandSay(answer=f"Command {Command} doesn't exist", color='WARNING')

except BaseException:
    import ErrorLoggingKit.Logger as logger
    logger.log_error(message="Command.py")
