from pynput.keyboard import Key, Controller

keyboard = Controller()

def VenvKey(KeyToPress=0):
    keyboard.press(key = KeyToPress)
    keyboard.release(key = KeyToPress)
