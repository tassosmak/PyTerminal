import time
import sys
def count_time():
    t = int(input("Enter the time in seconds: "))
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
count_time()
sys.exit()