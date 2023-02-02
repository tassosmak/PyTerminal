# SNC short for : SerialNumberCheck
import subprocess
from Kernel import credentials as cred
from Kernel.utils import edit_json, error_exit
from Kernel import flags


def run(cmd, Write=False):
    if not Write:
        try:
            Serial =  subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                        .stdout \
                        .strip()
            if not Serial == cred.SerialNum:
                # error_exit()
                from os import _exit
                _exit(1)
        except:
            return 
    elif Write:
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
            "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'",Write=write))
        else:
            run(
            "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'")

    if flags.pl == '2':
        if write:
            edit_json(loc1='user_credentials',loc2='Serial', content=run('wmic csproduct get uuid', Write=write))
        else:
            run('wmic csproduct get uuid')

    if flags.pl == '3':
        if write:
            edit_json(loc1='user_credentials',loc2='Serial', content=run('cat /var/lib/dbus/machine-id', Write=write))
        else:
            run('cat /var/lib/dbus/machine-id')