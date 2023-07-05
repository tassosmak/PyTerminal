#!/usr/bin/python3
try:
    from Kernel.ErrorLoggingKit import Logger as logger
    from Kernel.utils import args_help, set_flags
    from Kernel.SystemCalls import SystemCalls
    import Kernel.src.CallGraph as CallGraph
    from Kernel import ThreadHandler as TH
    from Kernel import credentials as cred
    from Kernel.UserHandler import loader
    from Kernel import flags
except:
    print('Kernel Error')
    from os import _exit
    _exit(0)

import sys
if __name__ == '__main__':
    import launcher
    
def MainTask():
    loader()
    while True:
        launcher.boot()

try:
    try:
        if str(sys.argv[1]) == 'Run':
            TH.run(MainTask)
        elif str(sys.argv[1]) == 'ClearErrors':
            SystemCalls.clear_error()
            
        elif str(sys.argv[1]) == 'ClearHistory':
            SystemCalls.clear_history()
            
        elif str(sys.argv[1]) == "SetFlags":
            cred._get_credentials()
            if flags.EnableIntSoft:    
                cred._get_propiatery(True)
                set_flags()
        
        elif str(sys.argv[1]) == 'FakeLogin':
            from Kernel.LoginKit.LoginUI import LoginHandler
            loader(False)
            LoginHandler.run()
            
        elif str(sys.argv[1]) == 'NoThread':
            flags.ThreadActivated = False
            CallGraph.call_graph_filtered(MainTask)
        
        elif str(sys.argv[1]) == 'ForgotPassword':
            cred._get_credentials()
            SystemCalls.show_pswd()
            
        else:
            args_help()            
    except IndexError: #An IndexError will happen if the user doesn't give any prompt and run's the file by it self
        args_help()
except:
    logger.log_error("boot.py")