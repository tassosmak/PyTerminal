#!/usr/bin/python3
try:
    from Kernel.utils import args_help, set_flags, SystemCalls
    from Kernel.ErrorLoggingKit import Logger as logger
    from Kernel import ThreadHandler as TH
    from Kernel import credentials as cred
    from Kernel.UserHandler import loader
    from Kernel import flags
except:
    try:
        from Kernel.ErrorLoggingKit import Logger as logger
        logger.log_error('Kernel Error | Boot.py')
    except:
        print('Kernel Error')
        from os import _exit
        _exit(1)

import sys    
if __name__ == '__main__':
    import launcher
    
def MainTask():
    #print("1 Main Threading")
    loader()
    while True:
        launcher.boot()
        
def NoThread():
    flags.ThreadActivated = False
    loader()
    while True:
        launcher.boot()
        TH.SecondaryTask()
        

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
            from Kernel.LoginKit.LoginUI import Login
            loader(False)
            Login.Verify()
            
        elif str(sys.argv[1]) == 'NoThread':
            NoThread()
            
        else:
            args_help()            
    except IndexError:
        args_help()
except:
    logger.log_error("boot.py")