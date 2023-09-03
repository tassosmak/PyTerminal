from ntfpy import NTFYServer, NTFYUser, NTFYClient, NTFYPushMessage, NTFYViewAction
from Kernel.SystemCalls import break_after
from Kernel import flags



@break_after(3)
def Sender(content):
    server = NTFYServer("http://100.65.44.143:8080")
    user = NTFYUser("tassosmak", "8596")
    client = NTFYClient(server, "PyTerminal_Information_System", user)
    action = NTFYViewAction("Github Link", "https://www.github.com/tassosmak/pyterminal")
    message = NTFYPushMessage(content)
    message.addAction(action)
    message.title = flags.Default_text
    # message.addTag("warning")
    client.send_message(message)