save_path = 'Kernel/ErrorLoggingKit'
fl_name = 'errors.log'

def log_error(message="NO_MSG"):
    #Init The File
    from Kernel import flags
    if flags.FTU == '1':
        from Kernel.ErrorLoggingKit.ErrorPreviewer import ErrorScreen
        from Kernel.RendererKit.HighlightKit.console import Console
        from Kernel.AudioKit import Audio
        from Kernel.utils import clear_screen, get_time
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
        logger.exception(f'\n{get_time(secs=True)} {message}\nHere is the error good luck solving it :)')
        ErrorScreen()
        if flags.EnableIntSoft:
            console.print_exception(show_locals=True)
        Audio.play('Kernel/AudioKit/src/Error.mp3')
    else:
        from Kernel.utils import clear_screen
        import sys
        clear_screen()
        sys.stdout.write('Error')
