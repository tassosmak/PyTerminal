import threading
import launcher
from pathlib import Path
import settings
 
def MainTask():
    #print("1 Main Threading")
    while True:
        launcher.boot()

        


base_folder = Path(__file__).parent.resolve()
Run = False
def SecondaryTask(file_name="0", stay_end=False):
    if Run:
        import os
        if settings.pl == "1":
            if stay_end:
                os.system(f"""osascript -e 'tell application "Terminal" to do script "python3 {base_folder}/src/{file_name}.py"'""")
            else:
                os.system(f"""osascript -e 'tell application "Terminal" to do script "python3 {base_folder}/src/{file_name}.py"'""")
                os.system("""osascript -e 'tell application "Terminal" to quit"'""")
        if settings.pl == "2":
            #print(type)
            if stay_end:
                os.system(f"start cmd /k py  src/{file_name}.py")
            else:
                os.system(f"start cmd /c py  src/{file_name}.py")


if __name__ == "__main__":

    t1 = threading.Thread(target=MainTask, name='t1')
    t2 = threading.Thread(target=SecondaryTask, name='t2')  

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    