from Kernel.ErrorLoggingKit import Logger as logger
from Kernel import flags
import threading
import subprocess



def SecondaryTask(file_name="0", stay_end=False):
    if not file_name=='0':
        import os
        if not flags.Inside_Thread:
            if flags.pl == "1":
                subprocess.run(f"""osascript -e 'tell application "Terminal" to do script "python3 {flags.base_folder}/src/{file_name}.py"'""", shell=True, capture_output=True, check=True, encoding="utf-8")
            elif flags.pl == "2":
                if stay_end:
                    os.system(f"start cmd /k py  src/{file_name}.py")
                else:
                    os.system(f"start cmd /c py  src/{file_name}.py")
            else:
                os.system(f"python3 {flags.base_folder}/src/{file_name}.py")
        else:
            os.system(f"python3 {flags.base_folder}/src/{file_name}.py")

def run(MainThread):
    try:
        t1 = threading.Thread(target=MainThread, name='t1')
        t2 = threading.Thread(target=SecondaryTask, name='t2')  
        
        t1.start()
        t2.start()
        while True:
            t1.join()
            t2.join()
    except BaseException:
        logger.log_error("boot.py")