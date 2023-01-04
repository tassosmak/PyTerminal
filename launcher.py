from ErrorLoggingKit import Logger as logger
from RendererKit import Renderer as RD
if not __name__ == '__main__':
    import Kernel as kernel
    from UserHandlingKit.UserHandler import init
    from UserHandlingKit.utils import edit_json, jump_mode
    import commands as cmd
from src import settings


def _run():
        try:
            kernel.core(MODE=settings.MODE, pl=settings.pl, username=settings.USERNAME)
        except IndexError:
            ask_new_md = input("it seems that the registered mode of user is corrupted\nwhat mode did you used\n1) The Basic Mode\n2)The Advanced Mode\nType below:\n")
            if ask_new_md == '9':
                settings.MODE = '2'
                ask_new_md = '2'
            edit_json(loc1='user_credentials', loc2='Mode', content=ask_new_md)
            edit_json(loc1='Internal-Software', loc2='Enable', content='0')
        if cmd.jump:
            jump_mode()
            kernel.core(MODE=settings.MODE, pl=settings.pl, username=settings.USERNAME)
            cmd.jump = False
        if cmd.logout:
            init()
            cmd.logout = False



def boot():
    try:
        #print(UserH.UserMD)
        _run()
    except KeyboardInterrupt:
        if settings.EnableIntSoft:
            RD.CommandQuest(type='2', msg='KeyboardInterrupt')
    except EOFError:
        if settings.EnableIntSoft:
            RD.CommandQuest(type='2', msg='EOFError')
    except BaseException:
        if settings.MODE == "9" or settings.MODE == "3":
            RD.CommandSay("There Was An Error see 'errors.log' in the Error_Manager Folder for more info", "FAIL")
            logger.log_error()
            from os import system, _exit
            if settings.pl == '1' or settings.pl == '3':
                system("killall python")
            else:
                _exit(1)
        else:
            if settings.EnableIntSoft:
                logger.log_error("IntSoft Enabled")
            RD.CommandSay("There Was An Error", "FAIL")
            from os import system, _exit
            if settings.pl == '1' or settings.pl == '3':
                system("killall python")
            else:
                _exit(1)