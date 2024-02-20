#!/usr/bin/python3
from Kernel.ErrorLoggingKit import Logger as logger
from Kernel.utils import args_help, set_flags
from Kernel.SystemCalls import SystemCalls
from Kernel import credentials as cred
from Kernel.UserHandler import loader
from Kernel import flags
import launcher

from sys import argv
flags.Runtype='local'
def MainTask():
    loader()
    while True:
        launcher.boot()

try:
    try:
        if str(argv[1]) == 'Run':
            # pass
            MainTask()
        elif str(argv[1]) == 'ClearErrors':
            SystemCalls.clear_error()
            
        elif str(argv[1]) == 'ClearHistory':
            SystemCalls.clear_history()
            
        elif str(argv[1]) == "SetFlags":
            loader(False)
            if flags.EnableIntSoft:    
                cred._get_propiatery(True)
                set_flags()
        
        elif str(argv[1]) == 'FakeLogin':
            from Kernel.LoginKit.LoginUI import LoginHandler
            loader(False)
            LoginHandler.run()
        
        elif str(argv[1]) == 'ForgotPassword':
            loader(False)
            SystemCalls.show_pswd()
            
        else:
            args_help()            
    except IndexError: #An IndexError will happen if the user doesn't give any prompt and run's the file by it self
        args_help()
except:
    logger.log_error("BootHandler")
