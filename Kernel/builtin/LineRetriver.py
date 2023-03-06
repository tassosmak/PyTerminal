from pathlib import Path

from src import utils
utils.add_depend()
from Kernel.RendererKit import Renderer as RD

try:
    import clipboard
except ModuleNotFoundError:
    from sys import exit
    RD.CommandSay("Clipboard Module Is missing", 'WARNING')
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
RD.CommandSay("DONE", 'OKGREEN')