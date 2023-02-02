import os
import sys

def run(cmd):
    try:
        os.system(cmd)
    except:
        return None

def guid():
    # print
    if sys.platform == 'darwin':
        return run(
        "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'",
        )

    if sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'msys':
        return run('wmic csproduct get uuid')

    if sys.platform.startswith('linux'):
        return run('cat /var/lib/dbus/machine-id') or \
            run('cat /etc/machine-id')
guid()