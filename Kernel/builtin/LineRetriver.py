from src import utils
utils.add_depend(str(utils.sys.argv[1]))
from Kernel.RendererKit import Renderer as RD
from Kernel import utils

try:
    import clipboard
except ModuleNotFoundError:
    RD.CommandSay("Clipboard Module Is missing", 'WARNING')
    utils.Exit.exit()

line_to_copy="0"
def Lastlines():
    global line_to_copy
    with open(f'{base_folder}/src/history.log', "r") as file:
        for line in (file.readlines() [-1:]):
            line_to_copy=line

base_folder = utils.get_folder()
Lastlines()
clipboard.copy(str(line_to_copy))
RD.CommandSay("DONE", 'OKGREEN')