import sys, os


def add_makro():
    sys_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    sys.path.insert(0, sys_path)

    from Makro.MakroCore import credentials as cred, utils, SystemCalls, flags
    utils.pl_finder()
    SystemCalls.SystemCalls.get_folder()
    cred.get_credentials(False, f'{flags.base_folder}/users/{str(sys.argv[1])}.json')
    utils.clear_screen()