from Makro.MakroCore.utils import ModeHandling as MoDeH, Exit
from Makro.MakroCore import ModeHandling as MDH #MDH for MODE HANDLING
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore.SystemCalls import SystemCalls
from Makro.MakroCore.FTU import FTU_init as FTU
from Makro.MakroCore.UserHandler import loader
from Makro.MakroCore import flags

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
        if flags.newuser:
            FTU().run()
            flags.newuser = False



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