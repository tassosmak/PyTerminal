from src import utils
utils.add_depend(str(utils.sys.argv[1]))
from Kernel.RendererKit.Renderer import CommandSay

CommandSay(answer='tested', color='OKGREEN')