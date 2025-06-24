from Kernel.NotificationsKit.ntfpy import NTFYServer, NTFYUser, NTFYClient, NTFYPushMessage, NTFYViewAction
from Kernel.SystemCalls import break_after
from Kernel import flags
from Kernel.CryptographyKit import utils



class Notifications():
    
    def __init__(self):
         pass
    
    @break_after(3)
    def Sender(self, content):
        self.server = NTFYServer("http://192.168.1.63:80")
        self.user = NTFYUser("tassosmak", "8596")
        self.client = NTFYClient(self.server, "PyTerminal_Information_System", self.user)
        self.action = NTFYViewAction("Github Link", "https://www.github.com/tassosmak/pyterminal")
        self.message = NTFYPushMessage(content)
        self.message.addAction(self.action)
        self.message.title = flags.Default_text
        # self.message.addTag("warning")
        self.client.send_message(self.message)
        return content

    def Code_Sender(self, num=4):
            self.code = utils._gen_safe_password(num)
            self.Sender(self.code)
            return self.code