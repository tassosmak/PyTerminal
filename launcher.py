if not __name__ == '__main__':
    from UserHandlingKit.utils import edit_json, jump_mode, error_exit
    from UserHandlingKit.UserHandler import init
    import Kernel as kernel
    import commands as cmd
from RendererKit import Renderer as RD
from src import flags


def _run():
        try:
            kernel.core(MODE=flags.MODE, pl=flags.pl, username=flags.USERNAME)
        except IndexError:
            ask_new_md = input("it seems that the registered mode of user is corrupted\nwhat mode did you used\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n")
            if ask_new_md == '9':
                flags.MODE = '2'
                ask_new_md = '2'
            edit_json(loc1='user_credentials', loc2='Mode', content=ask_new_md)
            edit_json(loc1='Internal-Software', loc2='Enable', content='0')
        if cmd.jump:
            jump_mode()
            kernel.core(MODE=flags.MODE, pl=flags.pl, username=flags.USERNAME)
            cmd.jump = False
        if cmd.logout:
            init()
            cmd.logout = False



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
        error_exit()