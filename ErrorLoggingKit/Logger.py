from ErrorLoggingKit.ErrorPreviewer import ErrorScreen
from RendererKit.HighlightKit.console import Console
from src import settings
import logging
import os
import datetime

save_path = 'ErrorLoggingKit'
console = Console()

def log_error(message="NO_MSG", fl_name="errors.log"):
    if not message == "KeyboardInterrupt":
        #Init The File
        logger = logging.getLogger('PyTerminal')
        logger.setLevel(logging.DEBUG)


        # create file handler which logs even debug messages
        fh = logging.FileHandler(os.path.join(save_path, fl_name))
        fh.setLevel(logging.DEBUG)
        logger.addHandler(fh)

        # Here Is The Actual Command That Types The Error :)
        now = datetime.datetime.now()
        logger.exception(f'\n{now.strftime("%Y-%m-%d %H:%M:%S")} {message}\nHere is the error good luck solving it :)')
        ErrorScreen()
        if settings.EnableIntSoft:
            console.print_exception(show_locals=True)
