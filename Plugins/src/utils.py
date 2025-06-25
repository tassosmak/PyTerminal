import sys

def add_depend(path):
    substring = "Kernel"
    fix_path = ""
    str_list = path.split(substring)
    for element in str_list:
        fix_path += element    
    
    sys.path.insert(0, fix_path)

    from Kernel import credentials as cred, utils
    utils.pl_finder()
    utils.clear_screen()
    cred.get_credentials(False, f'{path}/users/Default.json')
    