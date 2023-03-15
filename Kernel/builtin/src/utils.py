import sys

def add_depend(path):
    substring = "Kernel"
    fix_path = ""
    str_list = path.split(substring)
    for element in str_list:
        fix_path += element    
    
    sys.path.insert(0, fix_path)
    from Kernel import UserHandler as UserH
    UserH.loader(False)