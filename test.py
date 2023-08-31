from ntfpy import NTFYServer, NTFYUser, NTFYClient, NTFYPushMessage, NTFYViewAction

def main():
    server = NTFYServer("http://100.65.44.143:8080")
    user = NTFYUser("user", "pass")
    client = NTFYClient(server, "Test", user)
    message = NTFYPushMessage("With a cool button you can press", title = "This is also a test")
    message.addTag("beginner")
    action = NTFYViewAction("Github Link", "https://www.github.com/tassosmak/pyterminal")
    message.addAction(action)
    client.send_message(message)

if __name__ == "__main__":
    main()






