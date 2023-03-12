import ModeHandling as MDH #MDH for MODE HANDLING
from Kernel.RendererKit import Renderer as RD
from Kernel.UserHandler import loader
from Kernel import flags
from Kernel.utils import SystemCalls, Exit, recover_mode, jump_mode

@SystemCalls.measure_time
def _run():
        try:
            MDH.core()
        except IndexError:
            recover_mode()
        if flags.jump:
            jump_mode()
        if flags.logout:
            loader()
            flags.logout = False



def boot():
    try:
        _run()
    except KeyboardInterrupt:
        if flags.EnableIntSoft:
            RD.CommandQuest(type='2', msg='KeyboardInterrupt')
    except EOFError:
        if flags.EnableIntSoft:
            RD.CommandQuest(type='2', msg='EOFError')
        else:
            RD.CommandSay(answer='\n')
    except:
        Exit.error_exit()