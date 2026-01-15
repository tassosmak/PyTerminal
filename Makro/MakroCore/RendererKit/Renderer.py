"""
PyTerminal Rendering Library
"""

from Makro.Drivers.NotificationsKit import Alert, Buttons, Dialog, Icon

from Makro.MakroCore import flags, utils
try: 
    from Makro.MakroCore.RendererKit.HighlightKit import color_text
except: pass

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


class CommandShow:
    '''
    PyTerminal Rendering Library
    
    - Push: Notification
    - Choice: Dialog With Two Options
    - Info: Dialog just for Info-Warning's
    - Input: Dialog Where The User Types Text
    - Show: Works like a print just with colors
    '''
    
    Quest_result = ''
    
    def __init__(self, msg="Blank Request", header=flags.Default_text):
        if not header==flags.Default_text:
                header=f'{flags.Default_text} {header}'
        self.header = header
        self.msg = msg
        
    
    
    def Push(self):
        if flags.pl == '1' and flags.FTU == '1' and flags.EnableGUI == True:
            command = f'''
            osascript -e 'display notification "{self.msg}" with title "{self.header}"'
            '''
            os.system(command)
        else:
            CommandShow(f'Notification: {self.msg}').Show('OKGREEN')

    
    def Choice(self, Button1='No', Button2='Yes', Button3=None):
        global Quest_result
        if flags.EnableGUI:
                if flags.pl == '1':
                    if not Button3 == None:
                        al = Alert(self.msg).with_buttons(Buttons([Button1, Button2, Button3])).show()
                    else:
                        al = Alert(self.msg).with_buttons(Buttons([Button1, Button2])).show()

                    Quest_result = al.button_returned
        else:
            if not Button3 == None:
                Quest_result = input(f'{self.msg}, Type "{Button1}" or "{Button2}" or "{Button3}":')
            else:
                Quest_result = input(f'{self.msg}, Type "{Button1}" or "{Button2}":')
        return Quest_result
            
    def Info(self):
        global Quest_result
        if flags.EnableGUI:
            if flags.pl == '1':
                script = f"""
                display dialog "{self.msg}" with title "{self.header}" with icon note buttons "OK"
                """

                subprocess.call("osascript -e '{}'".format(script), shell=True, stdout=subprocess.DEVNULL)
        else:
            self.msg.removeprefix('( ) "" ')
            Quest_result = CommandShow(msg=self.msg).Show(color='WARNING')
            return Quest_result
            
    def Input(self):
        global Quest_result
        if flags.EnableGUI:
            if flags.pl == '1':
                buttons = Buttons(['Exit', 'Ok'])
                the_dialog = Dialog(self.msg)
                the_dialog.with_title(self.header)
                the_dialog.with_buttons(buttons)
                the_dialog.with_icon(Icon.NOTE)
                the_dialog.with_input()


                result = the_dialog.show()
                if result.button_returned == "Exit":
                    utils.Exit.exit()
                
                if flags.Fully_GUI == False:
                    if result.text_returned == 'exit':
                        utils.clear_gui()
                
                Quest_result = result.text_returned  # => text entered in input
        else:
            Quest_result = input(f"{self.msg}:")
        return Quest_result


    def Show(self, color='', legacy=False):
        if legacy == False and flags.FTU =='1':
            try:
                if "WARNING" in color: 
                    color_text.output(content=self.msg, args='Bold Yellow')
                elif "FAIL" in color:
                    color_text.output(content=self.msg, args='Bold Red')
                elif "OKGREEN" in color:
                    color_text.output(content=self.msg, args='Bold Green')
                elif "PURPLE" in color:
                    color_text.output(content=self.msg, args='Bold Purple')
                else:
                    color_text.output(content=self.msg, args=color)
            except: print(f'RendererKit Fallback | {self.msg}')
        else:
            try:
                if "WARNING" in color: 
                    print(f'{bcolors.WARNING}{self.msg}{bcolors.WHITE}')
                elif "FAIL" in color:
                    print(f'{bcolors.FAIL}{self.msg}{bcolors.WHITE}')
                elif "OKGREEN" in color:
                    print(f'{bcolors.OKGREEN}{self.msg}{bcolors.WHITE}')
                elif "PURPLE" in color:
                    print(f'{bcolors.PURPLE}{self.msg}{bcolors.WHITE}')
                else:
                    print(self.msg)
            except:
                print(self.msg)