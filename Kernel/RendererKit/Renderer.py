from Kernel.NotificationsKit import Alert, Buttons, Dialog, Icon

try: from Kernel.RendererKit.HighlightKit import color_text 
except: pass

from Kernel import flags, utils
import subprocess
import os

Quest_result = ''

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
    PURPLE = '\033[95m'
    DARKCYAN = '\033[36m'


def CommandPush(message, header=flags.Default_text):
    if flags.pl == '1' and flags.FTU == '1' and flags.EnableGUI == True:
        if not header==flags.Default_text:
            header=f'{flags.Default_text} {header}'
        command = f'''
        osascript -e 'display notification "{message}" with title "{header}"'
        '''
        os.system(command)
    else:
        CommandSay(answer=(f'Notification: {message}'))


def CommandQuest(type='0', Button1='No', Button2='Yes', msg="Blank Request", header=flags.Default_text):
    global Quest_result
    Quest_result = ''
    if type == '1':
        if flags.EnableGUI:
                al = Alert(msg).with_buttons(Buttons([Button1, Button2,])).show()

                Quest_result = al.button_returned
                return Quest_result
        else:
            Quest_result = input(f'{msg}, Type "{Button1}" or "{Button2}":')
            return Quest_result
    elif type == "2":
        if flags.EnableGUI:
            applescript = f"""
            display dialog "{msg}" with title "{header}" with icon caution buttons "OK"
            """

            subprocess.call("osascript -e '{}'".format(applescript), shell=True)
        else:
            msg.removeprefix('( ) "" ')
            Quest_result = CommandSay(answer=msg, color='WARNING')
    elif type == '3':
        if flags.EnableGUI:
            buttons = Buttons(["Ok"])
            the_dialog = Dialog(msg).with_title(header)
            the_dialog.with_buttons(buttons)
            the_dialog.with_icon(Icon.NOTE)
            the_dialog.with_input("Type Here:")

            result = the_dialog.show()
            
            if flags.Fully_GUI == False:
                if not result.text_returned == 'exit':
                    Quest_result = result.text_returned  # => text entered in input
                else:
                    utils.clear_gui()        
            else:
                Quest_result = result.text_returned
            return Quest_result
                
        else:
            Quest_result = input(f"{msg}:")


def CommandSay(answer=0, color='', legacy=False):
    if not flags.FTU == '2' or legacy == True:
        try:
            if "WARNING" in color: 
                color_text.output(content=answer, args='Bold Yellow')
            elif "FAIL" in color:
                color_text.output(content=answer, args='Bold Red')
            elif "OKGREEN" in color:
                color_text.output(content=answer, args='Bold Green')
            elif "PURPLE" in color:
                color_text.output(content=answer, args='Bold Purple')
            else:
                color_text.output(content=answer, args=color)
        except: print(answer)
    else:
        try:
            if "WARNING" in color: 
                print(f'{bcolors.WARNING}{answer}{bcolors.WHITE}')
            elif "FAIL" in color:
                print(f'{bcolors.FAIL}{answer}{bcolors.WHITE}')
            elif "OKGREEN" in color:
                print(f'{bcolors.OKGREEN}{answer}{bcolors.WHITE}')
            elif "PURPLE" in color:
                print(f'{bcolors.PURPLE}{answer}{bcolors.WHITE}')
            else:
                print(answer)
        except:
            print(answer)