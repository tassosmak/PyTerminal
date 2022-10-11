import threading
import time
import launcher
import commands as cmd
import subprocess
from pathlib import Path
 
def MainTask():
    print("1 Main Threading")
    while True:
        launcher.run()
base_folder = Path(__file__).parent.resolve()

def SecondaryTask(type="0"):
    import os
    os.system(f"""osascript -e 'tell application "Terminal" to do script "python3 {base_folder}/bb.py"'""")

    # if type == "countdown":
    #     t = int(input("Enter the time in seconds: "))
    #     while t:
    #         mins, secs = divmod(t, 60)
    #         timer = '{:02d}:{:02d}'.format(mins, secs)
    #         print(timer, end="\r")
    #         time.sleep(1)
    #         t -= 1

    
    







if __name__ == "__main__":

    t1 = threading.Thread(target=MainTask, name='t1')
    t2 = threading.Thread(target=SecondaryTask, name='t2')  
   
    t1.start()
    t2.start()

    t1.join()
    t2.join()