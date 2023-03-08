import os

def install(name=0):
    try: os.system(f"pip3 install {name}")
    except: raise MemoryError