from Kernel.utils import ModeHandling as MoDeH, Exit, SystemCalls
import ModeHandling as MDH #MDH for MODE HANDLING
from Kernel.RendererKit import Renderer as RD
from Kernel.UserHandler import loader
from Kernel import flags

@SystemCalls.measure_time
def _run():
        try:
            MDH.core()
        except IndexError:
            MoDeH.recover_mode()
        if flags.jump:
            MoDeH.jump_mode()
        if flags.logout:
            loader()
            flags.logout = False



def boot():
    try:
        _run()
    except KeyboardInterrupt:
        if flags.EnableIntSoft:
            RD.CommandQuest(msg='KeyboardInterrupt').Info()
    except EOFError:
        if flags.EnableIntSoft:
            RD.CommandQuest(msg='EOFError').Info()
        else:
            RD.CommandSay(answer='\n')
    except:
        Exit.error_exit()