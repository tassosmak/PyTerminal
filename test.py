import subprocess
import os
import sys

def run(cmd):
    try:
        # return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
        #                 .stdout \
        #                 .strip()
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
        return run('wmic csproduct get uuid').split('\n')[2] \
                                            .strip()

    if sys.platform.startswith('linux'):
        return run('cat /var/lib/dbus/machine-id') or \
            run('cat /etc/machine-id')

    if sys.platform.startswith('openbsd') or sys.platform.startswith('freebsd'):
        return run('cat /etc/hostid') or \
            run('kenv -q smbios.system.uuid')
guid()