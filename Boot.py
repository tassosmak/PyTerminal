try:
    from Kernel.utils import Clear, set_flags, args_help
    import Kernel.ErrorLoggingKit.Logger as logger
    from Kernel import credentials as cred
    from Kernel.UserHandler import init
    from Kernel import flags
except:
    print('Kernel is Missing')
    from os import _exit
    _exit(1)
    
if __name__ == '__main__':
    import launcher
from pathlib import Path
import threading
import sys

def MainTask():
    #print("1 Main Threading")
    init()
    while True:
        launcher.boot()
        


base_folder = Path(__file__).parent.resolve()
def SecondaryTask(file_name="0", stay_end=False):
    if not file_name=='0':
        import os
        if flags.pl == "1":
            if stay_end:
                os.system(f"""osascript -e 'tell application "Terminal" to do script "python3 {base_folder}/src/{file_name}.py"'""")
            else:
                os.system(f"""osascript -e 'tell application "Terminal" to do script "python3 {base_folder}/src/{file_name}.py"'""")
                os.system("""osascript -e 'tell application "Terminal" to quit"'""")
        elif flags.pl == "2":
            if stay_end:
                os.system(f"start cmd /k py  src/{file_name}.py")
            else:
                os.system(f"start cmd /c py  src/{file_name}.py")
        else:
            os.system(f"python3 {base_folder}/src/{file_name}.py")

try:
    if __name__ == "__main__":
        try:
            if str(sys.argv[1]) == 'Run':
                t1 = threading.Thread(target=MainTask, name='t1')
                t2 = threading.Thread(target=SecondaryTask, name='t2')  

                t1.start()
                t2.start()

                t1.join()
                t2.join()
                
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
                    flags.ThreadActivated = False
                    init()
                    while True:
                        launcher.boot()
                        SecondaryTask()
            else:
                args_help()            
        except IndexError:
            args_help()
except BaseException:
    logger.log_error("boot.py")