import threading
import time
import launcher
import commands as cmd
import subprocess
from pathlib import Path
import UserHandler as UserH
 
def MainTask():
    print("1 Main Threading")
    while True:
        launcher.run()


base_folder = Path(__file__).parent.resolve()

def SecondaryTask(type="0"):
    import os
    if UserH.pl == "1":
        os.system(f"""osascript -e 'tell application "Terminal" to do script "python3 {base_folder}/{type}.py"'""")



    
    







if __name__ == "__main__":

    t1 = threading.Thread(target=MainTask, name='t1')
    t2 = threading.Thread(target=SecondaryTask, name='t2')  
   
    t1.start()
    t2.start()

    t1.join()
    t2.join()