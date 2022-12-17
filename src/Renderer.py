from src import settings
import os
from NotificationsKit import Alert, Buttons, AlertType, Dialog, Icon
import subprocess
import sys

Quest_result = 0




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







def CommandQuest(type='0', Button1='No', Button2='Yes', error_msg="Blank", quest_msg='Blank', quest_icon=Icon.NOTE, ask_admin_msg="This Procces Require Administraive Access\n are you sure you want to grant it?"):
    global Quest_result
    Quest_result = 0
    if type == '1':
        if settings.EnableGUI:
                al = Alert(ask_admin_msg).with_buttons(Buttons([Button1, Button2,])).show()

                Quest_result = al.button_returned
        else:
            Quest_result = input(f'{ask_admin_msg}, Type "{Button1}" or "{Button2}":')
    elif type == "2":
        if settings.EnableGUI:
            applescript = f"""
            display dialog "{error_msg}" with title "{settings.Default_text}" with icon caution buttons "OK"
            """

            subprocess.call("osascript -e '{}'".format(applescript), shell=True)
        else:
            # print(quest_msg)
            quest_msg.removeprefix('( ) "" ')
            Quest_result = CommandSay(answer=error_msg, color='WARNING')
    elif type == '3':
        if settings.EnableGUI:
            buttons = Buttons(["Ok", "Exit"])
            the_dialog = Dialog(quest_msg).with_title(settings.Default_text)
            the_dialog.with_buttons(buttons)
            the_dialog.with_icon(quest_icon)
            the_dialog.with_input("Type Here:")

            result = the_dialog.show()

            Quest_result = result.text_returned  # => text entered in input
        else:
            Quest_result = input(f"{quest_msg}:")


def CommandSay(answer=0, color=0):
    if color == "WARNING":
        sys.stderr.write(f"\n{bcolors.WARNING}{answer}{bcolors.WHITE}\n")
    elif color == "FAIL":
        sys.stderr.write(f"\n{bcolors.FAIL}{answer}{bcolors.WHITE}\n")
    elif color == "OKGREEN":
        sys.stderr.write(f"\n{bcolors.OKGREEN}{answer}{bcolors.WHITE}\n")
    elif color == "PURPLE":
        sys.stderr.write(f"\n{bcolors.PURPLE}{answer}{bcolors.WHITE}\n")
    else:
        sys.stderr.write(f"\n{answer}\n")