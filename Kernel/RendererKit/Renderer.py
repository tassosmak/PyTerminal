from Kernel.NotificationsKit import Alert, Buttons, Dialog, Icon
from Kernel.RendererKit.HighlightKit import color_text
from Kernel import flags
import subprocess
import os

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
    if flags.pl == '1' and flags.FTU == '1':
        command = f'''
        osascript -e 'display notification "{message}" with title "{header}"'
        '''
        os.system(command)
    else:
        CommandSay(message)


def CommandQuest(type='0', Button1='No', Button2='Yes', quest_icon=Icon.NOTE, msg="Blank Request", header=flags.Default_text):
    global Quest_result
    Quest_result = ''
    if type == '1':
        if flags.EnableGUI:
                al = Alert(msg).with_buttons(Buttons([Button1, Button2,])).show()

                Quest_result = al.button_returned
        else:
            Quest_result = input(f'{msg}, Type "{Button1}" or "{Button2}":')
    elif type == "2":
        if flags.EnableGUI:
            applescript = f"""
            display dialog "{msg}" with title "{header}" with icon caution buttons "OK"
            """

            subprocess.call("osascript -e '{}'".format(applescript), shell=True)
        else:
            # print(quest_msg)
            msg.removeprefix('( ) "" ')
            Quest_result = CommandSay(answer=msg, color='WARNING')
    elif type == '3':
        if flags.EnableGUI:
            buttons = Buttons(["Ok"])
            the_dialog = Dialog(msg).with_title(header)
            the_dialog.with_buttons(buttons)
            the_dialog.with_icon(quest_icon)
            the_dialog.with_input("Type Here:")

            result = the_dialog.show()

            Quest_result = result.text_returned  # => text entered in input
        else:
            Quest_result = input(f"{msg}:")


def CommandSay(answer=0, color=''):
    if not flags.FTU == '2':
        if color == "WARNING":
            color_text.output(content=answer, args='Bold Yellow')
        elif color == "FAIL":
            color_text.output(content=answer, args='Bold Red')
        elif color == "OKGREEN":
            color_text.output(content=answer, args='Bold Green')
        elif color == "PURPLE":
            color_text.output(content=answer, args='Bold Purple')
        else:
            color_text.output(content=answer, args=color)
    else:
        print(answer)