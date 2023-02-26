from Kernel.RendererKit import Renderer as RD
from Kernel.UserHandler import loader
from Kernel import flags, utils
import ModeHandling as kernel


def _run():
        try:
            kernel.core(MODE=flags.MODE)
        except IndexError:
            utils.recover_mode()   
        if flags.jump:
            utils.jump_mode()
        if flags.logout:
            loader()
            flags.logout = False



def boot():
    try:
        #print(UserH.UserMD)
        _run()
    except KeyboardInterrupt:
        if flags.EnableIntSoft:
            RD.CommandQuest(type='2', msg='KeyboardInterrupt')
    except EOFError:
        if flags.EnableIntSoft:
            RD.CommandQuest(type='2', msg='EOFError')
        else:
            RD.CommandSay(answer='\n')
    except BaseException:
        utils.Exit.error_exit()