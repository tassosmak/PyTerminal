import sys

def add_depend(path):
    substring = "Makro/MakroCore"
    fix_path = ""
    str_list = path.split(substring)
    for element in str_list:
        fix_path += element    
    
    sys.path.insert(0, fix_path)

    from Makro.MakroCore import credentials as cred, utils, SystemCalls
    utils.pl_finder()
    utils.clear_screen()
    SystemCalls.SystemCalls.get_folder()
    cred.get_credentials(False, f'{path}/users/Default.json')
    