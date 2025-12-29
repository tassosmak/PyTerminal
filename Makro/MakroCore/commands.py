'''
The Command List
'''
from Makro.Drivers.NotificationsKit.PushSender import Notifications
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore.KernelReboot import KernelReboot
from Makro.MakroCore.utils import clear_screen, Exit
from Makro.MakroCore.SystemCalls import SystemCalls
from Makro.MakroCore import TaskHandler, flags
from Makro.Drivers.AudioKit import Audio
from Makro.MakroCore.src import registry
from Makro.MakroCore import utils

import sys
import os

def CommandList(Command=str):
    try:
        global ask_recv
        if flags.EnableIntSoft and flags.Run_Straight_Builtin and flags.MODE == '9':
            TaskHandler.SecondaryTask(Command)
            return
        else:
            if not Command in flags._CML and not Command in flags._ACML:
                if not Command == '' :
                    if flags.EnableIntSoft:
                        RD.CommandShow(f"This Commmand Isn't registered with The PyTerminal CML or ACML").Show("FAIL")
                        flags.LCommand = '0'
                        return
                    else:
                        RD.CommandShow(f'Command {Command} Does Not Exist').Show('WARNING')
                        flags.LCommand = '0'
                        return
                else:
                    flags.LCommand = '0'
            else:
                flags.LCommand = Command

        if Command == "ls":
            if not flags.safe_md:
                if flags.MODE == "9":
                    RD.CommandShow(SystemCalls.get_fl_content(flags.base_folder)).Show()
                else:
                    RD.CommandShow("This Function isn't available within this mode").Show("WARNING")

        if Command == "test":
            if flags.MODE == "9":
                TaskHandler.SecondaryTask(file_name="test", stay_end=True)
                Notifications().Sender('Testing')
                RD.CommandShow('tested','tested').Push()
                RD.CommandShow(msg="tested").Show()
                RD.CommandShow(msg="tested").Show("WARNING")
                RD.CommandShow(msg="tested").Show('FAIL')
                RD.CommandShow(msg="tested").Show('OKGREEN')
                RD.CommandShow(msg="tested").Show('PURPLE')
                RD.CommandShow(msg="tested").Show('BLUE')
                RD.CommandShow(msg=f'Tested {SystemCalls.get_time()}').Info()
                RD.CommandShow(msg=RD.CommandShow(msg='Testing').Input()).Show(color="WARNING")
                if RD.CommandShow(msg="tested").Choice() == 'Yes':
                    RD.CommandShow(msg='Positive msg').Show(color='WARNING')
                else:
                    RD.CommandShow(msg='Negative msg').Show('WARNING')
                Audio.play('Makro/MakroCore/AudioKit/src/Boot.mp3')

        if Command == "about" or Command == "version":
            RD.CommandShow(flags.Version).Push()


        if Command == "time":
            RD.CommandShow(f'The time is: {SystemCalls.get_time(date=False)}').Push()

        if Command == "del" or Command == "delete":
            if not flags.safe_md:
                if flags.MODE == "2" or flags.MODE == '9':
                    RD.CommandShow(SystemCalls.get_fl_content())
                    try:
                        os.remove(RD.CommandShow(msg="what file you want to delete:").Input())
                        RD.CommandShow(msg="DONE").Show(color="OKGREEN")
                    except FileNotFoundError:
                        RD.CommandShow(msg="This file doesn't exist").Info()
                else:
                    RD.CommandShow(msg="This Function isn't available within this mode").Info()

        if Command == "create":
            if not flags.safe_md:
                if not flags.MODE == '1':
                        ask_name = RD.CommandShow(msg="What the name of the file you want to create?").Input()
                        try:
                            open(ask_name, "x")
                            RD.CommandShow(msg="DONE").Info()
                        except FileExistsError:
                            RD.CommandShow(msg="This file already exist do you want to delete it?").Choice()
                            if "yes" in RD.Quest_result.lower():
                                os.remove(f'{flags.base_folder}/../{ask_name}')
                                RD.CommandShow(msg="DONE").Info()
                        except UnboundLocalError:
                                pass
                else:
                    RD.CommandShow(msg="What the name of the file you want to create?").Input()
                    try:
                        open(RD.Quest_result, "x")
                        RD.CommandShow(msg="DONE").Show(color="OKGREEN")
                    except FileExistsError:
                        RD.CommandShow(msg="This file already exist try again").Info()
                    except UnboundLocalError:
                        RD.CommandShow(msg="There was a Problem try again").Info()

        if Command == "latest":
            TaskHandler.SecondaryTask(file_name="LineRetriver")


        if Command == "gen password":
            TaskHandler.SecondaryTask(file_name="Password_Gen")


        if Command == "exit":
            if flags.MODE == "1":
                RD.CommandShow(msg="Are you sure you want to exit?").Choice('Yes', 'No')
                if RD.Quest_result.lower() == 'yes':
                    Exit.exit()
            else:
                Exit.exit()


        if Command == "jump":
            if not flags.safe_md:
                flags.jump = True


        if Command == "print md":
            if not flags.safe_md:
                RD.CommandShow(msg=flags.MODE).Show()
            else:
                RD.CommandShow("You Are in Native-Mode").Show('WARNING')



        if Command == "talk":
            if not flags.safe_md:
                if flags.net:
                    from Makro.Plugins import Server, client
                    RD.CommandShow(msg='do you want to be host or reciever').Choice(Button1='Host', Button2='Talker')
                    #ask_type = input("do you want to be host or reciever\nif you want to be host press 1 otherwise prees 2")
                    if RD.Quest_result == "Host":
                        Server.chat()
                    elif RD.Quest_result == "Talker":
                        #ask_recv = input("To Which IP you want to talk to\nType Below!\n:")
                        RD.CommandShow(msg='To Which IP you want to talk to Type Below!').Input()
                        ask_recv = str(RD.Quest_result)
                        try:
                            client.Chat(IP=ask_recv)
                        except:
                            if not RD.Quest_result == '':
                                RD.CommandShow(msg="This User is Unavilable at the moment\ntry again later").Show(color="WARNING")
                            else: pass
                else:
                    RD.CommandShow(msg="You Are in Safe Mode you can't connect to the internet right now").Show()



        if Command == "clear":
            clear_screen()

        if Command == "view file":
            if flags.EnableIntSoft and flags.pl == '1':
                TaskHandler.SecondaryTask('view_file')
            else:
                RD.CommandShow(msg='type the name of the file you want to view').Input()
                #ask_file = input("type the name of the file you want to view\n:")
                if flags.pl == "1" or flags.pl == "3":
                    if not RD.Quest_result in flags.file_list:
                        os.system(f"cat {RD.Quest_result}")
                elif flags.pl == "2":
                    if not RD.Quest_result in flags.file_list:
                        os.system(f"notepad {RD.Quest_result}")

        if Command == "edit file":
            if not flags.safe_md:
                if flags.MODE == "2" or flags.MODE == '9':
                    if flags.pl == "1" or flags.pl == "3":
                        RD.CommandShow(msg='Type the name of the file you want to edit').Input()
                        if not RD.Quest_result in flags.file_list:
                            #ask_file = input("type the name of the file you want to edit\n:")
                            if RD.Quest_result.endswith(".py"):
                                os.system(f"vim {RD.Quest_result}")
                            else:
                                os.system(f"nano {RD.Quest_result}")
                    elif flags.pl == "2":
                        RD.CommandShow(msg='Type the name of the file you want to edit').Input()
                        if not RD.Quest_result in flags.file_list:
                            os.system(f'notepad {RD.Quest_result}')
                else:
                    RD.CommandShow(msg="This Function isn't available within this mode").Show(color="FAIL")

        if Command == "weather forecast":
            if not flags.safe_md:
                if flags.net:
                    os.system("curl wttr.in/")
                    RD.CommandShow(msg="This is a fork from @igor_chubin").Show(color="OKGREEN")
                else:
                    RD.CommandShow(msg="You Are in Safe Mode so you can't connect to the internet right now").Show()

        if Command == "activity monitor":
            if not flags.safe_md:
                if flags.MODE == "2" or flags.MODE == "9":
                    if flags.pl == "1" or flags.pl == "3":
                        TaskHandler.SecondaryTask('top')
                else:
                    RD.CommandShow(msg="This Function isn't available within this mode").Show(color="FAIL")

        if Command == "countdown":
            TaskHandler.SecondaryTask(file_name="countdown")



        if Command == "check site status":
            if not flags.safe_md:
                if flags.MODE == "2" or flags.MODE == "9":
                    RD.CommandShow("Type The Adress Of The Site You Want To Check", 'Down Detecter').Input()
                    os.system(f"ping {RD.Quest_result} -c 4")

                else:
                    RD.CommandShow(msg="This Function isn't available within this mode").Show('WARNING')



        if Command == "logout":
            flags.logout = True

        if Command == 'chatbox':
            if flags.net:
                TaskHandler.SecondaryTask('chatgpt')
        if Command == 'chatbox install':
            if not flags.safe_md:
                if flags.net:
                    os.system('python3 src/chatgpt.py install')
                    clear_screen()

        if Command == 'infostats':
            if not flags.safe_md:
                if flags.EnableIntSoft:
                    clear_screen()
                    RD.CommandShow(msg=flags.Default_text).Show('PURPLE')
                    RD.CommandShow('').Show()
                    RD.CommandShow(msg=sys.version).Show('OKGREEN')
                    RD.CommandShow('').Show()
                    RD.CommandShow(msg=("Platform ID: " + flags.pl)).Show(color='BLUE')
                    RD.CommandShow(msg=("Username: " + flags.USERNAME)).Show('BLUE')
                    RD.CommandShow(msg="\nFlags Below:").Show('Bold Green')
                    RD.CommandShow(("UserLess Connection", flags.UserLess_Connection)).Show()
                    RD.CommandShow(("GO TO FTU", flags.GO_TO_FTU)).Show()
                    RD.CommandShow(("Fully GUI", flags.Fully_GUI)).Show()
                    RD.CommandShow(("Inside_Thread", flags.Inside_Thread)).Show()
                else:
                    from Makro.MakroCore.credentials import get_credentials
                    MODE = flags.MODE
                    get_credentials(True, f'{flags.base_folder}/users/{flags.USERNAME}.json')
                    flags.MODE = MODE

        if Command == "show cmd" or Command == 'show apps' or Command == 'help':
            RD.CommandShow(msg='Available Commands').Show('OKGREEN')
            RD.CommandShow(msg=flags._CML).Show('BLUE')
            if flags.EnableIntSoft:
                RD.CommandShow(msg='Available Advanced Commands').Show('OKGREEN')
                RD.CommandShow(msg=flags._ACML).Show('BLUE')

        if Command == "registry":
            if flags.MODE == '9':
                registry.regedit()

        if Command == 'browser':
            if flags.pl == '1':
                TaskHandler.SecondaryTask('Browser')
            else:
                RD.CommandShow(msg='Not Supported').Show('WARNING')

        if Command == 'ofp':
            if flags.EnableIntSoft and flags.MODE == '9':
                RD.CommandShow('Check The Launced Window').Show()
                TaskHandler.SecondaryTask('OFP')

        if Command == 'show flags':
            if not flags.safe_md:
                if flags.EnableIntSoft:
                    clear_screen()
                    Notifications().Sender(SystemCalls.show_flags())

        if Command == 'converter':
            TaskHandler.SecondaryTask('temp_mesuare_converter', stay_end=True)

        if Command == 'calculator':
            TaskHandler.SecondaryTask('calculator')

        if Command == 'stocks':
            TaskHandler.SecondaryTask('stock_viewer')

        if Command == 'most used commands':
            if not flags.safe_md:
                SystemCalls.most_used_commands()

        if Command == 'fake_error':
            if flags.EnableIntSoft:
                raise KeyError

        if Command == 'toquel':
            if flags.EnableIntSoft and flags.MODE == '9':
                import webbrowser
                Notifications().Sender('Mannn You Got Somee taste in music🤝')
                webbrowser.open_new('https://www.youtube.com/watch?v=iz-xxDJNCA4')

        if Command == 'plugins':
            if not flags.safe_md:
                plugin_exist = False
                while not plugin_exist:
                    RD.CommandShow(SystemCalls.get_fl_content('/../Plugins')).Show('BLUE')
                    if not RD.CommandShow('What plugin you want to load?').Input() == 'exit':
                        if os.path.isfile(f'{flags.base_folder}/../Plugins/{RD.Quest_result}.py'):
                            TaskHandler.SecondaryTask(RD.Quest_result)
                            plugin_exist = True
                        else:
                            clear_screen()
                            RD.CommandShow("This Plugin Doesn't Exist").Show('WARNING')
                    else:plugin_exist = True
        
        if Command == 'create user':
            if not flags.safe_md:
                flags.newuser = True

        if Command == 'remove user':
            if not flags.safe_md:
                if not flags.MODE == '1':
                    RD.CommandShow('Type the username you want to remove').Input()
                    if os.path.isfile(f'{flags.base_folder}/users/{RD.Quest_result}.json'):
                        if not RD.Quest_result == flags.USERNAME or RD.Quest_result == 'default':
                            os.remove(f'{flags.base_folder}/users/{RD.Quest_result}.json')
                            RD.CommandShow(msg=f'User {RD.Quest_result} Removed Successfully').Show('OKGREEN')
                        else:
                            RD.CommandShow(msg='You Can Not Remove Yourself!').Info()
                    else:
                        RD.CommandShow(msg='This User Does Not Exist').Show('WARNING')
                else:
                    RD.CommandShow(msg='This Function is not available in this mode').Show('WARNING')
        
        if Command == 'change account type':
            if not flags.safe_md:
                RD.CommandShow(msg='there are 2 Modes on this terminal').Choice(Button1='The Advanced Mode', Button2='The Basic Mode')
                if RD.Quest_result == 'The Advanced Mode' or RD.Quest_result == '2':
                    ask_Mode = '2'
                elif RD.Quest_result == 'The Basic Mode' or RD.Quest_result == '1':
                    ask_Mode = '1'
                elif RD.Quest_result == '9':
                    ask_Mode = '9'
                else:
                    ask_Mode = '1'
                utils.edit_user_config(
                    username=flags.USERNAME,
                    Loc1='user_credentials',
                    Loc2='Mode',
                    Content=ask_Mode
                )
                RD.CommandShow(msg=f'Account Type Changed Successfully').Show('OKGREEN')



        if Command == 'change password':
            if not flags.safe_md:
                if not flags.UserLess_Connection:
                    from Makro.MakroCore.LoginKit.LoginUI import LoginHandlerUserStore as lgh
                    enc_password = lgh().ask_password()
                    if enc_password == flags.PASSWORD:
                        new_pswd = RD.CommandShow('Type your new password').Input()
                        RD.CommandShow(f'Your new password is: {RD.Quest_result}').Info()
                        from Makro.MakroCore.CryptographyKit import EncryptPassword as encrypt
                        utils.edit_user_config(
                            username=flags.USERNAME,
                            Loc1='user_credentials',
                            Loc2='Password',
                            Content=encrypt.encrypt_password(password=new_pswd, save=False)
                        )
                        RD.CommandShow(msg='Password Changed Successfully').Show('OKGREEN')
                else:
                    RD.CommandShow(msg='You Are in UserLess Mode').Show('WARNING')
                    
        if Command == 'makro reload':
            if not flags.safe_md:
                if flags.EnableIntSoft:
                    reloader = KernelReboot()
                    if reloader.reload_all():
                        RD.CommandShow(msg='Makro Reloaded Successfully').Show('OKGREEN')
                    else:
                        RD.CommandShow(msg='Makro Reload Failed').Show('FAIL')

        if Command == 'password manager':
            TaskHandler.SecondaryTask('Password_Manager')
            
        if Command == 'clear gui':
            if not flags.safe_md:
                if flags.EnableIntSoft:
                    utils.clear_gui()

    except: Exit.error_exit()