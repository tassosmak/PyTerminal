# SNC short for : SerialNumberCheck

from Kernel.RendererKit import Renderer as RD
from Kernel import credentials as cred
from Kernel.utils import edit_json
from Kernel import flags
import subprocess


def run(cmd, Write=False):
    if Write == False:
        # try:
            Serial =  subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                        .stdout \
                        .strip()
            if not Serial == cred.SerialNum:
                raise IndexError
        # except:
            # return 
    elif Write == True:
        try:
            return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                        .stdout \
                        .strip()
        except:
            return None

def guid(write=False):
    if flags.pl == '1':
        if write:
            edit_json(loc1='user_credentials',loc2='Serial', content=run(
            "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'",Write=True))
        else:
            run(
            "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'")

    if flags.pl == '2':
        if write:
            edit_json(loc1='user_credentials',loc2='Serial', content=run('wmic csproduct get uuid', Write=True))
        else:
            run('wmic csproduct get uuid')

    if flags.pl == '3':
        if write:
            edit_json(loc1='user_credentials',loc2='Serial', content=run('cat /var/lib/dbus/machine-id', Write=True))
        else:
            run('cat /var/lib/dbus/machine-id')