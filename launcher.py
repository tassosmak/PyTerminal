from Kernel.utils import ModeHandling as MoDeH, Exit
import ModeHandling as MDH #MDH for MODE HANDLING
from Kernel.RendererKit import Renderer as RD
from Kernel.SystemCalls import SystemCalls
from Kernel.UserHandler import loader
from Kernel import flags

@SystemCalls.Grapher
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
            RD.CommandShow(msg='KeyboardInterrupt').Info()
    except EOFError:
        if flags.EnableIntSoft:
            RD.CommandShow(msg='EOFError').Info()
        else:
            RD.CommandShow('\n').Show()
    except:
        Exit.error_exit()