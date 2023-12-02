from ntfpy import NTFYServer, NTFYUser, NTFYClient, NTFYPushMessage, NTFYViewAction
# from Kernel.SystemCalls import break_after
from Kernel import flags
from Kernel.CryptographyKit import utils



# @break_after(3)
def Sender(content):
    server = NTFYServer("http://192.168.1.63:80")
    user = NTFYUser("tassosmak", "8596")
    client = NTFYClient(server, "PyTerminal_Information_System", user)
    action = NTFYViewAction("Github Link", "https://www.github.com/tassosmak/pyterminal")
    message = NTFYPushMessage(content)
    message.addAction(action)
    message.title = flags.Default_text
    # message.addTag("warning")
    client.send_message(message)
    return content

def Code_Sender(num=4):
        code = utils._gen_safe_password(num)
        Sender(code)
        return code