from pathlib import Path
import os
try:
    import clipboard
except ModuleNotFoundError:
    from sys import exit
    print("Clipboard Module Is missing")
    exit()

line_to_copy="0"
def Lastlines(filename=0, Num_Lines=0, folder=0):
    global line_to_copy
    with open(folder/filename) as file:
         
        for line in (file.readlines() [-Num_Lines:]):
            line_to_copy=line

print(Path(__file__).parent.resolve())
fname = 'history.log'
N = 1
#Lastlines(filename=fname, Num_Lines=N, folder=base_folder)
clipboard.copy(str(line_to_copy))
print("DONE")
pass