save_path = 'Kernel/ErrorLoggingKit'
fl_name = 'errors.log'

def log_error(message="NO_MSG"):
    #Init The File
    from Kernel import flags
    if flags.FTU == '1':
        from Kernel.ErrorLoggingKit.ErrorPreviewer import ErrorScreen
        from Kernel.RendererKit.HighlightKit.console import Console
        from Kernel.AudioKit import Audio
        import datetime
        import logging
        import os
        console = Console()
        
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
        if flags.EnableIntSoft:
            console.print_exception(show_locals=True)
        Audio.play('Kernel/AudioKit/src/Error.mp3')
    else:
        import sys
        from Kernel import utils
        utils.clear_screen()
        sys.stdout.write('Error')
