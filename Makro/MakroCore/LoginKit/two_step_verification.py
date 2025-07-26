from Makro.Drivers.NotificationsKit.PushSender import Notifications
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags


class TwoStepVerification:
    def two_step_verification(self):
        verified = False
        if not flags.pl == '2':
            try:
                code = Notifications().Code_Sender()
            except:
                RD.CommandShow(msg='Makro Servers are down currently').Show('FAIL')
                from Makro.MakroCore.utils import Exit
                Exit.exit()
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