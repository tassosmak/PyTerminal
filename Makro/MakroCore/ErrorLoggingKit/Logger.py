save_path = 'Makro/MakroCore/ErrorLoggingKit'
fl_name = 'errors.log'

def log_error(message="NO_MSG"):
    #Init The File
    from Makro.MakroCore import flags
    if not flags.FTU == '2':
        from Makro.MakroCore.ErrorLoggingKit.ErrorPreviewer import ErrorScreen
        from Makro.MakroCore.RendererKit.HighlightKit.console import Console
        from Makro.Drivers.NotificationsKit.PushSender import Notifications
        from Makro.MakroCore.SystemCalls import SystemCalls
        from Makro.Drivers.AudioKit import Audio
        from io import StringIO
        import logging
        import os

        log_stream = StringIO()
        logging.basicConfig(stream=log_stream, level=logging.DEBUG)
        console = Console()
        
        logger = logging.getLogger('PyTerminal')


        # create file handler which logs even debug messages
        fh = logging.FileHandler(os.path.join(save_path, fl_name))
        fh.setLevel(logging.DEBUG)
        logger.addHandler(fh)

        # Here Is The Actual Command That Types The Error :)
        logger.exception(f'\n{SystemCalls.get_time(secs=True)} {message}\nHere is the error good luck solving it :)')
        
        
        if flags.EnableIntSoft:
            try:
                Notifications().Sender(log_stream.getvalue())
            except: print('Error Sending Error_Notification')
        
        
        ErrorScreen()
        
        
        if flags.EnableIntSoft:
            console.print_exception(show_locals=True)
        else:
            Audio.play('Drivers/AudioKit/src/Error.mp3')
    else:
        print('Error')
