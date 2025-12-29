import sys, os


def add_makro():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    sys.path.insert(0, path)
    username = str(sys.argv[2])

    from Makro.MakroCore import credentials as cred, utils, SystemCalls
    utils.pl_finder()
    SystemCalls.SystemCalls.get_folder()
    cred.get_credentials(False, f'{path}/Makro/MakroCore/users/{username}.json')
    utils.clear_screen()