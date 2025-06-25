from Drivers.NotificationsKit.PushSender import Notifications
from Kernel.RendererKit import Renderer as RD
from Kernel import flags


class TwoStepVerification:
    def two_step_verification(self):
        verified = False
        if not flags.pl == '2':
            code = Notifications().Code_Sender()
            while not verified:
                if flags.Fully_GUI and flags.MODE == '9':
                    ask_code = RD.CommandShow('We Have Send A code to your Phone').Input()
                    if ask_code == code:
                        verified = True
                else:
                    ask_code = input('We Have Send A code to your Phone')
                    if ask_code == code:
                        verified = True
        else:
            RD.CommandShow("Development Mode isn't supported on Windows").Show('WARNING')
            flags.EnableIntSoft = False