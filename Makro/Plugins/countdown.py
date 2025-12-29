from src import utils
utils.add_makro()
from Makro.MakroCore.RendererKit import Renderer as RD
import time

RD.CommandShow("Enter the time in seconds").Input()
t = int(RD.Quest_result)
while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
RD.CommandShow('Your Countdown Has Ended', 'Countdown').Push()