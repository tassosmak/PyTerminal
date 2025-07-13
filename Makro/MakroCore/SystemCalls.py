'''
Main API
========
PyTerminal System Calls
'''

from Makro.MakroCore.utils import pl_finder, clear_gui, args_help
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags
from pathlib import Path
import datetime
import signal
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
    
    def get_fl_content(path=flags.base_folder):
        if path != flags.base_folder:
            if flags.pl == '1' or flags.pl == '3':
                path = f'{flags.base_folder}/{path}'
            else:
                path = f'{flags.base_folder}\\{path}'
        # List all .py files and remove the .py extension
        py_files = [
            os.path.splitext(f)[0]
            for f in os.listdir(path)
            if f.endswith(".py") and os.path.isfile(os.path.join(path, f))
        ]
        return py_files
        
    def measure_time(func):
        def wrapper():
            if flags.Runtime_Tracer:
                pre = time.time()
                func()
                after = time.time() -pre
                after = round(after, 2)
                if flags.MODE == '9':
                    RD.CommandShow(msg=f'Time Passed: {after} Seconds').Show('PURPLE')
            else: func()
        return wrapper

    """A Call Tree Graph Generator"""
    def Grapher(func):
        output_png="Makro/MakroCore/src/CallGraph.png"
        custom_include=None
        def wrapper():
            if flags.Create_Graph and '1' in flags.FTU:
                from pycallgraph2 import GlobbingFilter, PyCallGraph, Config
                from pycallgraph2.output import GraphvizOutput
                config = Config()
                config.trace_filter = GlobbingFilter(include=custom_include)
                graphviz = GraphvizOutput(output_file=output_png)
                with PyCallGraph(output=graphviz, config=config):
                            func()
            else:
                func()
        return wrapper

    def clear_error():
        pl_finder()
        clear_file = open("MakroCore/ErrorLoggingKit/errors.log",'w')
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
            if not Command in flags._ACML:
                if not Command == 'jump':
                    with open(f'{flags.base_folder}/src/history.log', 'a') as f:
                        f.write(str(f'{SystemCalls.get_time()} | {Command}\n'))

    def show_flags(print=True):
        result = []
        for arg in flags.all_variables:
            if not arg.startswith('_'):
                value = eval(f'flags.{arg}')
                output = arg, type(value), value
                if print:
                    RD.CommandShow(msg=output).Show(color='BLUE')
                result.append(output)
        return str(result)
    
    def show_pswd():
        """This Idiot Forgot His Password"""
        if flags.EnableIntSoft:
            try: 
                from Makro.MakroCore.CryptographyKit.decrypt import Decryptor as DC
                RD.CommandShow(DC(flags.PASSWORD).decrypt_password()).Info()
            except ImportError: args_help()
            
    def most_used_commands():
        with open(f"{flags.base_folder}/src/history.log", "r") as file:
            data = file.read()
            for i in flags._CML:
                occurrences = data.count(i)
                RD.CommandShow(f"{i}: {occurrences}").Show(color='BLUE')
                

class TimeoutException(Exception):   # Custom exception class
    pass

def break_after(seconds=5):
    def timeout_handler(signum, frame):   # Custom signal handler
        raise TimeoutException
    def function(function):
        def wrapper(*args, **kwargs):
            if flags.pl == '1' or flags.pl =='3': 
                signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(seconds)
                try:
                    res = function(*args, **kwargs)
                    signal.alarm(0)      # Clear alarm
                    return res
                except TimeoutException:
                    if flags.EnableIntSoft:
                        RD.CommandShow(f'Timeou reached | Function name: {function.__name__}').Show('YELLOW')
                return
            else: return function
        return wrapper
    return function