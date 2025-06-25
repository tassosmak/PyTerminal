#!/usr/bin/python3
from Makro.MakroCore.ErrorLoggingKit import Logger as logger
from Makro.MakroCore.utils import args_help, set_flags
from Makro.MakroCore.SystemCalls import SystemCalls
from Makro.MakroCore import credentials as cred
from Makro.MakroCore.UserHandler import loader
from Makro.Boot import launcher
from Makro.MakroCore import flags

import commands as cmd
flags.Module = cmd.CommandList

from sys import argv

def MainTask():
    loader()
    while True:
        launcher.boot()

try:
    try:
        if str(argv[1]) == 'Run':
            MainTask()
        elif str(argv[1]) == 'ClearErrors':
            SystemCalls.clear_error()

        elif str(argv[1]) == 'ClearHistory':
            SystemCalls.clear_history()

        elif str(argv[1]) == "SetFlags":
            loader(False)
            if flags.EnableIntSoft:
                cred._get_propiatery()
                set_flags()

        elif str(argv[1]) == 'FakeLogin':
            from Makro.MakroCore.LoginKit.login_handler import LoginHandler
            loader(False)
            LoginHandler.run()

        elif str(argv[1]) == 'ForgotPassword':
            loader(False)
            SystemCalls.show_pswd()

        else:
            args_help()
    except IndexError: #An IndexError will happen if the user doesn't give any prompt and run's the file by it self
        args_help()
except:
    logger.log_error("BootHandler")
