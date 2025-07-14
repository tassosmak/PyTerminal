"""PyTerminal SNC(SerialNumberCheck) Library"""
# SNC short for : SerialNumberCheck

from Makro.MakroCore.utils import edit_user_config
from Makro.MakroCore import credentials as cred
from Makro.MakroCore import flags
import subprocess

class PlatformError(Exception):
    pass


class snc:
    def __init__(self, write=False):
        self.write = write
        
    def run(self):
        if self.write == False:
            Serial =  subprocess.run(self.cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                        .stdout \
                        .strip()
            if not Serial == cred.SerialNum:
                raise IndexError
        else:
            try:
                return subprocess.run(self.cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                            .stdout \
                            .strip()
            except:
                return None

    def guid(self, USERNAME):
        if flags.pl == '1':
            if self.write == True:
                self.cmd = "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'"
                edit_user_config(username=USERNAME, Loc1='user_credentials', Loc2='Serial', Content=self.run())
            else:
                self.cmd = "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'"
                self.run()

        elif flags.pl == '2':
            if self.write:
                self.cmd = 'wmic csproduct get uuid'
                edit_user_config(username=USERNAME, Loc1='user_credentials',Loc2='Serial', Content=self.run())
            else:
                self.cmd = 'wmic csproduct get uuid'
                self.run()

        elif flags.pl == '3':
            if self.write:
                self.cmd = 'cat /var/lib/dbus/machine-id'
                edit_user_config(username=USERNAME, Loc1='user_credentials', Loc2='Serial', Content=self.run())
            else:
                self.cmd = 'cat /var/lib/dbus/machine-id'
                self.run()
        else:
            raise PlatformError