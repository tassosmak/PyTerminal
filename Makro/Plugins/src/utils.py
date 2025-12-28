import os, sys, platform

def _pl_finder():
    pl = platform.platform()
    if pl.startswith("macOS"):
        return "1"
    elif pl.startswith("Windows"):
        return "2"
    elif pl.startswith("Linux"):
        return "3"


def add_depend(path):
    pl = _pl_finder()
    if not pl == "2":
        substring = "Makro/MakroCore"
        fix_path = ""
        str_list = path.split(substring)
        for element in str_list:
            fix_path += element
        
        sys.path.insert(0, fix_path)
    else:
        PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        sys.path.insert(0, PROJECT_ROOT)
    

    from Makro.MakroCore import credentials as cred, utils, SystemCalls
    utils.pl_finder()
    SystemCalls.SystemCalls.get_folder()
    cred.get_credentials(False, f'{path}/users/default.json')
    utils.clear_screen()