import socket


def Chat(IP=0):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_IP = IP
    PORT = 5050
    ADDR = (SERVER_IP, PORT)
    client.connect(ADDR)

    if client.recv(2048).decode("utf-8") == "Server":
        print("Server Talk Enabled :)")
        while True:
            answer = client.recv(2048).decode("utf-8")
            print(answer)
    else:    
        while True:
            message = 0
            if message == "Exit":
                break
            message = input("Type Your message below\n").encode("utf-8")
            client.send(message)
            answer = client.recv(2048).decode("utf-8")
            print(answer)
        