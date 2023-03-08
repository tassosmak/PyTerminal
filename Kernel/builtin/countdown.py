from src import utils
utils.add_depend(str(utils.sys.argv[1]))
from Kernel.RendererKit import Renderer as RD
import time

def count_time():
    RD.CommandQuest(type='3', msg="Enter the time in seconds")
    t = int(RD.Quest_result)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
count_time()