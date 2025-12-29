from src import utils
utils.add_makro()
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore.SystemCalls import SystemCalls
from Makro.MakroCore import utils

try:
    import clipboard
except ModuleNotFoundError:
    RD.CommandShow("Clipboard Module Is missing").Show('WARNING')
    utils.Exit.exit()

line_to_copy="0"
def Lastlines():
    global line_to_copy
    with open(f'{base_folder}/src/history.log', "r") as file:
        for line in (file.readlines() [-1:]):
            line_to_copy=line

base_folder = SystemCalls.get_folder()
Lastlines()
clipboard.copy(str(line_to_copy))
RD.CommandShow("DONE").Show('OKGREEN')