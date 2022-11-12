from pathlib import Path
import os
os.system("ls")
try:
    import clipboard
except ModuleNotFoundError:
    from sys import exit
    print("Clipboard Module Is missing")
    exit()

line_to_copy="0"
def Lastlines():
    global line_to_copy
    with open(f'{base_folder}/history.log', "r") as file:
        for line in (file.readlines() [-1:]):
            line_to_copy=line

base_folder = Path(__file__).parent.resolve()
Lastlines()
clipboard.copy(str(line_to_copy))
print("DONE")