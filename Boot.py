try:
    from Kernel.utils import args_help, Clear, set_flags
    from Kernel.ErrorLoggingKit import Logger as logger
    from Kernel import ThreadHandler as TH
    from Kernel import credentials as cred
    from Kernel.UserHandler import init
    from Kernel import flags
except:
    print('Kernel Error')
    from os import _exit
    _exit(1)
from pathlib import Path
import sys    
if __name__ == '__main__':
    import launcher
    
def MainTask():
    #print("1 Main Threading")
    init()
    while True:
        launcher.boot()
        
def NoThread():
    flags.ThreadActivated = False
    init()
    while True:
        launcher.boot()
        TH.SecondaryTask()
        
        
flags.base_folder = Path(__file__).parent.resolve()
try:
    try:
        if str(sys.argv[1]) == 'Run':
            TH.run(MainTask)
        elif str(sys.argv[1]) == 'ClearErrors':
            Clear.clear_error()
            
        elif str(sys.argv[1]) == 'ClearHistory':
            Clear.clear_history()
            
        elif str(sys.argv[1]) == "SetFlags":
            cred._get_credentials()
            if flags.EnableIntSoft:    
                cred._get_propiatery(True)
                set_flags()
        
        elif str(sys.argv[1]) == 'FakeLogin':
            init()
            
        elif str(sys.argv[1]) == 'NoThread':
            NoThread()
            
        else:
            args_help()            
    except IndexError:
        args_help()
except BaseException:
    logger.log_error("boot.py")