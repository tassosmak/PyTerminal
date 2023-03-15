try:
    '''
    Adding Modules from The Kernel
    '''
    from Kernel.utils import Exit, SystemCalls, clear_screen
    from Kernel.RendererKit import Renderer as RD
    from Kernel import ThreadHandler, flags
    from Kernel.AudioKit import Audio
    from Kernel.src import registry
    
    import sys
    import os

    def CommandList(Command=str, safe_md=False):
        global ask_recv, LCommand
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
            if flags.MODE == "9":
                RD.CommandSay(answer=os.listdir(flags.base_folder))
            else:
                RD.CommandSay(answer="This Function isn't available within this mode", color="WARNING")

        if Command == "test":
            if flags.MODE == "9":
                if not flags.pl == "3":
                    ThreadHandler.SecondaryTask(file_name="test", stay_end=True)
                RD.CommandSay(answer="tested")
                RD.CommandSay(answer="tested", color="WARNING")
                RD.CommandSay(answer="tested", color="FAIL")
                RD.CommandSay(answer="tested", color="OKGREEN")
                RD.CommandSay(answer="tested", color="PURPLE")
                RD.CommandSay(answer="tested", color="BLUE")
                RD.CommandQuest(type='2', msg=f'Tested {SystemCalls.get_time()}')
                RD.CommandQuest(type='3', msg='Testing')
                RD.CommandSay(answer=RD.Quest_result, color="WARNING")
                RD.CommandQuest(type='1', msg="tested")
                if RD.Quest_result == 'Yes':
                    RD.CommandSay(answer='Positive answer', color='WARNING')
                else:
                    RD.CommandSay(answer='Negative answer', color='WARNING')
                Audio.play('Kernel/AudioKit/src/Boot.mp3')
            else:
                RD.CommandSay(answer="tested")
        
        if Command == "about" or Command == "version": 
            RD.CommandSay(answer="PyTerminal V.Beta by Makro Software", color='OKGREEN')
        
        
        if Command == "time":
            RD.CommandPush(f'The time is: {SystemCalls.get_time(date=False)}')

        if Command == "del" or Command == "delete":
            if not safe_md:
                if flags.MODE == "2" or flags.MODE == '9':
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
                if flags.MODE == "1":
                    RD.CommandQuest(type='3', msg="What the name of the file you want to create?")
                    try:
                        open(RD.Quest_result, "x")
                        RD.CommandSay(answer="DONE", color="OKGREEN")
                    except FileExistsError:
                        RD.CommandQuest(type='2', msg="This file already exist try again")
                    except UnboundLocalError:
                        RD.CommandQuest(type='2', msg="There was a Problem try again")
                elif flags.MODE == "2" or flags.MODE == "9":
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
            ThreadHandler.SecondaryTask(file_name="LineRetriver")
            

        if Command == "gen password":
            if not safe_md:
                ThreadHandler.SecondaryTask(file_name="Password_Gen")


        if Command == "exit":
            if flags.MODE == "1":
                ask_exit = input("Are you sure. if yes press 'Y' and hit return")
                if ask_exit == "Y" or ask_exit == "y":
                    Exit.exit()
            elif flags.MODE == "2" or flags.MODE == "9" or flags.MODE == "3":
                Exit.exit()


            
        if Command == "jump":
            if not safe_md:
                flags.jump = True


        if Command == "print md":
            if not safe_md:
                RD.CommandSay(answer=flags.MODE)
            else:
                RD.CommandSay("You Are in Native-Mode", color='WARNING')



        if Command == "talk":
            if not safe_md:
                if flags.net:
                    from Kernel.builtin import Server, client
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
                ThreadHandler.SecondaryTask('view_file')
            else:
                RD.CommandQuest(type='3', msg='type the name of the file you want to view')
                #ask_file = input("type the name of the file you want to view\n:")
                if flags.pl == "1" or flags.pl == "3":
                    if not RD.Quest_result in flags.file_list:
                        os.system(f"cat {RD.Quest_result}")
                elif flags.pl == "2":
                    if not RD.Quest_result in flags.file_list:
                        os.system(f"more {RD.Quest_result}")
        
        if Command == "edit file":
            if not safe_md:
                if flags.MODE == "2" or flags.MODE == '9':           
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
                if flags.MODE == "2" or flags.MODE == "9":
                    if flags.pl == "1" or flags.pl == "3":
                        ThreadHandler.SecondaryTask('top')
                else:
                    RD.CommandSay(answer="This Function isn't available within this mode", color="FAIL")

        if Command == "countdown":
            if not safe_md:
                ThreadHandler.SecondaryTask(file_name="countdown")
                
            
        
        if Command == "check site status":
            if flags.MODE == "2" or flags.MODE == "9":
                RD.CommandQuest(type='3', msg="type the site you want to check:\n")
                os.system(f"ping {RD.Quest_result}")
                
            else:
                RD.CommandSay(answer="This Function isn't available within this mode", color="FAIL")


        if Command == "devices":
            if not safe_md:
                if not flags.pl == "2":
                    flags.FTU = '2'
                    if flags.FTU == "2":
                        import Kernel.NetworkingKit.server
                    else:
                        import Kernel.NetworkingKit.auth
                        if Kernel.NetworkingKit.auth.DONE:
                            ThreadHandler.SecondaryTask(file_name="Handle-External-Devices")
                else:
                    RD.CommandSay("NetworkingKit Isn't Supported On Windows")

        if Command == "logout":
            clear_screen()
            flags.logout = True
                
        if Command == 'chatbox':
            if not safe_md:
                if flags.net:
                    ThreadHandler.SecondaryTask('chatgpt')
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
                    RD.CommandSay(("Fully GUI", flags.Fully_GUI))
                    RD.CommandSay(("Threading", flags.ThreadActivated))
                    RD.CommandSay(("Inside_Thread", flags.Inside_Thread))
                else:
                    from Kernel import credentials as cred
                    MODE = flags.MODE
                    cred._get_credentials(True)
                    flags.MODE = MODE
        
        if Command == "show cmd" or Command == 'show apps' or Command == 'help':
            if flags.EnableIntSoft:
                RD.CommandSay(flags.CML, color='BLUE')
            else:
                RD.CommandSay('Available Commands', 'OKGREEN')
                RD.CommandSay(answer=os.listdir(flags.base_folder/'builtin'))
        
        if Command == "registry":
            if flags.MODE == '9':
                registry.regedit()
        
        if Command == 'browser':
            if not safe_md:
                if flags.pl == '1':
                    ThreadHandler.SecondaryTask('Browser')
                else:
                    RD.CommandSay(answer='Not Supported', color='WARNING')
        
        if Command == 'ofp':
            if not safe_md:
                if flags.EnableIntSoft and flags.MODE == '9':
                    RD.CommandSay('Check The Launced Window')
                    ThreadHandler.SecondaryTask('OFP')
                    
        if Command == 'show args':
            if not safe_md:
                if flags.MODE == '9':
                    clear_screen()
                    SystemCalls.show_flags()
            

except:
    Exit.error_exit()