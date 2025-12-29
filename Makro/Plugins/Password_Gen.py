from random import shuffle, choice
import string

from src.utils import add_makro, sys
add_makro()
from Makro.MakroCore.FlagsCaller import CallHandler as CH
from Makro.MakroCore.RendererKit import Renderer as RD

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
RD.CommandShow(msg="How long do you want your password to be").Input()
length = int(RD.Quest_result)
shuffle(characters)
password = []
for i in range(length):
    password.append(choice(characters))
password_str = ''.join(str(e) for e in password)
# RD.CommandSay(answer=("".join(password)), color='OKGREEN')
password = ''.join(password)
RD.CommandShow(f'Your Password Is: {password}').Push()
RD.CommandShow(msg="Would You like to export the password to a text file").Choice()
if 'yes' in RD.Quest_result.lower():
    with open(f"{CH.get_base_folder()}/../password.txt", "w") as f:
        f.write(password_str)
    RD.CommandShow('The File Is Saved', 'Password Generator').Push()
    from subprocess import call 
    file_to_show = f"{CH.get_base_folder()}/../Password.txt"
    call(["open", "-R", file_to_show])