import os

def install(name=0, show=False):
    try:
        if show:
            os.system(f"pip3 install {name}")
        else:
            os.system(f"pip3 install -q {name}")
    except: raise MemoryError