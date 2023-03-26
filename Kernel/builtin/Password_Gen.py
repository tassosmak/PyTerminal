from random import shuffle, choice
import string

from src.utils import add_depend, sys
add_depend(str(sys.argv[1]))
from Kernel.RendererKit import Renderer as RD
from Kernel import flags

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
RD.CommandQuest(type='3', msg="How long do you want your password to be")
length = int(RD.Quest_result)
shuffle(characters)
password = []
for i in range(length):
    password.append(choice(characters))
password_str = ''.join(str(e) for e in password)
# RD.CommandSay(answer=("".join(password)), color='OKGREEN')
password = ''.join(password)
RD.CommandPush(message=(f'Your Password Is: {password}'))
RD.CommandQuest(type='1', msg="Would You like to export the password to a text file")
if RD.Quest_result == "Yes":
    with open(f"{flags.base_folder}/../password.txt", "w") as f:
        f.write(password_str)
    RD.CommandPush('The File Is Saved')