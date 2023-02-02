try:
    from Kernel.utils import edit_json, clear_screen, error_exit
    from Kernel.RendererKit import Renderer as RD
    from pathlib import Path
    from Kernel import flags
    import datetime
    import Boot
    import sys
    import os

    '''
    Adding Modules From Different Folders
    '''
    try:
        from src import Server
        from src import client
        flags.net = True
    except OSError:
        print("\nunfortunately due to many instanches running at the same time it's not possible to connect to the network\nso the browsing expirience is unavailable\n")
        flags.net = False



    dir = Path(__file__).parent.resolve()
    jump = False
    logout = False

    def CommandAsk(plt=0, USNAME_PRINT=0, safe_mode=False, MD='0'):
        if MD == "2":
            CommandList(Command=input(f"!History isn't enabled! PyTerminal Beta | {flags.USERNAME.capitalize()} % "), cmd_pl=flags.pl, MD=flags.MODE)
        elif MD == "9": 
            CommandList(Command=input(f"PyTerminal {flags.sys_detect.system} | {flags.sys_detect.machine} % "), cmd_pl=flags.pl, MD=flags.MODE)
        elif MD == "3":
            CommandList(Command=input(f"PyTerminal | Safe-Mode $ "), cmd_pl=flags.pl, safe_md=safe_mode, MD=flags.MODE)
        else:
            CommandList(Command=input(f"PyTerminal Beta | {flags.USERNAME.capitalize()} $ "), cmd_pl=flags.pl, MD=flags.MODE) 


    def CommandList(Command=0, cmd_pl=0, safe_md=False, MD=0):
        global jump, logout, ask_recv, LCommand
        Command = Command.lower()
        if not Command in flags.CML:
                if not Command == '' :
                    if flags.EnableIntSoft:
                        RD.CommandSay(f"This Commmand Isn't registered with The PyTerminal CML", "FAIL")
                        LCommand = '0'
                        return
                    else:
                        RD.CommandSay(f'Command {Command} Does Not Exist', 'WARNING')
                        LCommand = '0'
                        return
                else:
                    LCommand = '0'
        else:
            LCommand = Command

        if Command == "ls":
            if MD == "2":
                RD.CommandSay(answer=os.listdir(dir))
            else:
                RD.CommandSay(answer="This Function isn't available within this mode", color="WARNING")

        if Command == "test":
            if MD == "9":
                RD.CommandSay(answer="tested")
                RD.CommandSay(answer="tested", color="WARNING")
                RD.CommandSay(answer="tested", color="FAIL")
                RD.CommandSay(answer="tested", color="OKGREEN")
                RD.CommandSay(answer="tested", color="PURPLE")
                RD.CommandSay(answer="tested", color="BLUE")
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
        
        if Command == "about" or Command == "version": 
            RD.CommandSay(answer="PyTerminal V.Beta by Makro Software")
        
        
        if Command == "time":
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
                    RD.CommandQuest(type='2', msg="This Function isn't available within this mode")

        if Command == "create":
            if not safe_md:
                if MD == "1":
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
                Boot.SecondaryTask(file_name="Password_Gen", stay_end=True)


        if Command == "exit":
            if MD == "1":
                ask_exit = input("Are you sure. if yes press 'Y' and hit return")
                if ask_exit == "Y" or ask_exit == "y":
                    os._exit(1)
            elif MD == "2" or MD == "9" or MD == "3":
                os._exit(1)

            
        if Command == "jump":
            if not safe_md:
                jump = True


        if Command == "print md":
            if not safe_md:
                RD.CommandSay(answer=MD)
            else:
                RD.CommandSay("You Are in Safe-Mode", color='WARNING')



        if Command == "talk":
            if not safe_md:
                if flags.net:
                    RD.CommandQuest(type='1', msg='do you want to be host or reciever', Button1='Host', Button2='Talker')
                    #ask_type = input("do you want to be host or reciever\nif you want to be host press 1 otherwise prees 2")
                    if RD.Quest_result == "Host":
                        Server.chat()
                    elif RD.Quest_result == "Talker":
                        #ask_recv = input("To Which IP you want to talk to\nType Below!\n:")
                        RD.CommandQuest(type='3', msg='To Which IP you want to talk to Type Below!')
                        ask_recv = str(RD.Quest_result)
                        try: 
                            client.Chat(IP=ask_recv)
                        except:
                            if not RD.Quest_result == '':
                               RD.CommandSay(answer="This User is Unavilable at the moment\ntry again later", color="WARNING")
                            else:
                               pass 
                else:
                    RD.CommandSay(answer="You Are in Safe Mode you can't connect to the internet right now")



        if Command == "clear":
            clear_screen()

        if Command == "view file":
            if flags.EnableIntSoft and flags.pl == '1':
                Boot.SecondaryTask('view_file')
            else:
                RD.CommandQuest(type='3', msg='type the name of the file you want to view')
                #ask_file = input("type the name of the file you want to view\n:")
                if cmd_pl == "1" or cmd_pl == "3":
                    if not RD.Quest_result in flags.file_list:
                        os.system(f"cat {RD.Quest_result}")
                elif cmd_pl == "2":
                    if not RD.Quest_result in flags.file_list:
                        os.system(f"more {RD.Quest_result}")
        
        if Command == "edit file":
            if not safe_md:
                if MD == "2" or MD == '9':           
                    if flags.pl == "1" or flags.pl == "3":
                        RD.CommandQuest(type='3', msg='Type the name of the file you want to edit')
                        if not RD.Quest_result in flags.file_list:
                            #ask_file = input("type the name of the file you want to edit\n:")
                            if RD.Quest_result.endswith(".py"):
                                os.system(f"vim {RD.Quest_result}")
                            else:
                                os.system(f"nano {RD.Quest_result}")
                    elif flags.pl == "2":
                        RD.CommandQuest(type='3', msg='Type the name of the file you want to edit')
                        if not RD.Quest_result in flags.file_list:
                            os.system(f'notepad {RD.Quest_result}')
                else:
                    RD.CommandSay(answer="This Function isn't available within this mode", color="FAIL")
        
        if Command == "weather forecast":
            if not safe_md:
                if flags.net:
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
                    RD.CommandSay(answer="This Function isn't available within this mode", color="FALI")

        if Command == "countdown":
            if not safe_md:
                Boot.SecondaryTask(file_name="countdown", stay_end=False)
                
            
        
        if Command == "check site status":
            if MD == "2" or MD == "9":
                RD.CommandQuest(type='3', msg="type the site you want to check:\n")
                os.system(f"ping {RD.Quest_result}")
                
            else:
                RD.CommandSay(answer="This Function isn't available within this mode", color="FALI")


        if Command == "devices":
            if not safe_md:
                if not cmd_pl == "2":
                    if flags.FTU == "2":
                        import Kernel.NetworkingKit.server
                    else:
                        import Kernel.NetworkingKit.auth
                        if Kernel.NetworkingKit.auth.DONE:
                            Boot.SecondaryTask(file_name="Handle-External-Devices", stay_end=True)
                else:
                    RD.CommandSay("NetworkingKit Isn't Supported On Windown")



        if Command == "logout":
            logout = True
            clear_screen()
                
                
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
                if flags.net:
                    Boot.SecondaryTask('chatgpt')
        if Command == 'chatbox install':
            if not safe_md:
                if flags.net:
                    os.system('python3 src/chatgpt.py install')
                    clear_screen()
        
        if Command == 'infostats':
            if not safe_md:
                if flags.EnableIntSoft:
                    clear_screen()
                    RD.CommandSay(answer=flags.Default_text, color='PURPLE')
                    RD.CommandSay('')
                    RD.CommandSay(answer=sys.version, color='OKGREEN')
                    RD.CommandSay('')
                    RD.CommandSay(answer=("Platform ID: " + flags.pl), color='BLUE')
                    RD.CommandSay(answer=("Username: " + flags.USERNAME), color='BLUE')
                    RD.CommandSay(answer="\nFlags Below:", color='Bold Green')
                    RD.CommandSay(("UserLess Connection", flags.UserLess_Connection))
                    RD.CommandSay(("GO TO FTU", flags.GO_TO_FTU))
                    RD.CommandSay(("Threading", flags.ThreadActivated))
        
        if Command == "show cmd":
            if not safe_md:
                if flags.EnableIntSoft:
                    RD.CommandSay(flags.CML, color='BLUE')
except BaseException:
    error_exit()