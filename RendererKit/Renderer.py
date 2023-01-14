from src import settings
import os
from NotificationsKit import Alert, Buttons, Dialog, Icon
import subprocess
import sys
from RendererKit import Highlight

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









def CommandPush(message, header=settings.Default_text):
    if settings.pl == '1':
        command = f'''
        osascript -e 'display notification "{message}" with title "{header}"'
        '''
        os.system(command)







def CommandQuest(type='0', Button1='No', Button2='Yes', quest_icon=Icon.NOTE, msg="Blank Request"):
    global Quest_result
    Quest_result = ''
    if type == '1':
        if settings.EnableGUI:
                al = Alert(msg).with_buttons(Buttons([Button1, Button2,])).show()

                Quest_result = al.button_returned
        else:
            Quest_result = input(f'{msg}, Type "{Button1}" or "{Button2}":')
    elif type == "2":
        if settings.EnableGUI:
            applescript = f"""
            display dialog "{msg}" with title "{settings.Default_text}" with icon caution buttons "OK"
            """

            subprocess.call("osascript -e '{}'".format(applescript), shell=True)
        else:
            # print(quest_msg)
            msg.removeprefix('( ) "" ')
            Quest_result = CommandSay(answer=msg, color='WARNING')
    elif type == '3':
        if settings.EnableGUI:
            buttons = Buttons(["Ok", "Exit"])
            the_dialog = Dialog(msg).with_title(settings.Default_text)
            the_dialog.with_buttons(buttons)
            the_dialog.with_icon(quest_icon)
            the_dialog.with_input("Type Here:")

            result = the_dialog.show()

            Quest_result = result.text_returned  # => text entered in input
        else:
            Quest_result = input(f"{msg}:")


def CommandSay(answer=0, color=0):
    if color == "WARNING":
        Highlight.output(content=answer, args='Bold Yellow')
    elif color == "FAIL":
        Highlight.output(content=answer, args='Bold Red')
    elif color == "OKGREEN":
        Highlight.output(content=answer, args='Bold Green')
    elif color == "PURPLE":
        Highlight.output(content=answer, args='Bold Purple')
    else:
        Highlight.output(content=answer, args='')