import termios
import sys
import fcntl
import os

def getKeyCode(blocking = True):
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    if not blocking:
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    try:
        return ord(sys.stdin.read(1))
    except IOError:
        return 0
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        if not blocking:
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def getKeyStroke():
    code  = getKeyCode()
    if code == 27:
        code2 = getKeyCode(blocking = False)
        if code2 == 0:
            return "esc"
        elif code2 == 91:
            code3 = getKeyCode(blocking = False)
            if code3 == 65:
                return "up"
            elif code3 == 66:
                return "down"
            elif code3 == 68:
                return "left"
            elif code3 == 67:
                return "right"
            else:
                return "esc?"
    elif code == 127:
        return "backspace"
    elif code == 9:
        return "tab"
    elif code == 10:
        return "return"
    elif code == 195 or code == 194:        
        code2 = getKeyCode(blocking = False)
        return chr(code)+chr(code2) # utf-8 char
    else:
        return chr(code)


while True:
    print(getKeyStroke())