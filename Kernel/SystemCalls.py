'''
Main API
========
PyTerminal System Calls
'''

from Kernel.RendererKit import Renderer as RD
from pathlib import Path
from Kernel import flags
from Kernel.utils import pl_finder, clear_gui, args_help
import datetime
import time
import os

class SystemCalls:   
    def get_time(date=True, secs=False):
        now = datetime.datetime.now()
        if date:
            if secs:
                return now.strftime("%Y-%m-%d %H:%M:%S")
            else:
                return now.strftime("%Y-%m-%d %H:%M")
        else:
            return now.strftime("%H:%M")

    def get_folder():
        flags.base_folder = Path(__file__).parent.resolve()
        return flags.base_folder
    
    def get_fl_contents():
        fl_contents = os.listdir(flags.base_folder)
        return fl_contents
    
    def measure_time(func):
        def wrapper():
            pre = time.time()
            func()
            after = time.time() -pre
            after = round(after, 2)
            if flags.MODE == '9':
                RD.CommandShow(msg=f'Time Passed: {after} Seconds').Show('PURPLE')
        return wrapper

    def clear_error():
        pl_finder()
        clear_file = open("Kernel/ErrorLoggingKit/errors.log",'w')
        clear_file.close()
        if flags.pl == '1':
           clear_gui()
        
    def clear_history():
        try:
            clear_file = open(f"{flags.base_folder}/src/history.log",'w')
            clear_file.close()    
        except FileNotFoundError:
            SystemCalls.get_folder()
            clear_file = open(f"{flags.base_folder}/src/history.log",'w')
            clear_file.close()

    def append_to_history(Command):
        if not Command == '0':
            if not 'jump' in Command:
                with open(f'{flags.base_folder}/src/history.log', 'a') as f:
                    f.write(str(f"{Command}\n"))

    def show_flags():
        for arg in flags.all_variables:
            if not arg.startswith('_'):
                value = eval(f'flags.{arg}')
                output = arg, type(value), value
                RD.CommandShow(msg=output).Show(color='BLUE', legacy=True)
    
    def show_pswd():
        #This Idiot Forgot His Password
        if flags.EnableIntSoft:
            try: 
                from Kernel.CryptographyKit import DecryptPassword
                RD.CommandShow(DecryptPassword.decrypt_password(flags.PASSWORD)).Show('BLUE', True)
            except ImportError: args_help()