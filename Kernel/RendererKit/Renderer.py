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


class CommandQuest:
    Quest_result = ''
    
    def __init__(self, Button1='No', Button2='Yes', msg="Blank Request", header=flags.Default_text):
        self.Button1 = Button1
        self.Button2 = Button2
        self.msg = msg
        self.header = header
    
    
    def Choice(self):
        global Quest_result
        if flags.EnableGUI:
                al = Alert(self.msg).with_buttons(Buttons([self.Button1, self.Button2,])).show()

                Quest_result = al.button_returned
        else:
            Quest_result = input(f'{self.msg}, Type "{self.Button1}" or "{self.Button2}":')
        return Quest_result
            
    def Info(self):
        global Quest_result
        if flags.EnableGUI:
            if not self.header==flags.Default_text:
                self.header=f'{flags.Default_text} {self.header}'
            script = f"""
            display dialog "{self.msg}" with title "{self.header}" with icon note buttons "OK"
            """

            subprocess.call("osascript -e '{}'".format(script), shell=True)
        else:
            self.msg.removeprefix('( ) "" ')
            Quest_result = CommandSay(answer=self.msg, color='WARNING')
            return Quest_result
            
    def Input(self):
        global Quest_result
        if flags.EnableGUI:
            buttons = Buttons(["Ok"])
            if not self.header==flags.Default_text:
                self.header=f'{flags.Default_text} {self.header}'
            the_dialog = Dialog(self.msg).with_title(self.header)
            the_dialog.with_buttons(buttons)
            the_dialog.with_icon(Icon.NOTE)
            the_dialog.with_input("Type Here:")

            result = the_dialog.show()
            
            if flags.Fully_GUI == False:
                if result.text_returned == 'exit':
                    utils.clear_gui()
            
            Quest_result = result.text_returned  # => text entered in input
                
        else:
            Quest_result = input(f"{self.msg}:")
        return Quest_result


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