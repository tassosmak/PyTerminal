import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_IP = "192.168.1.61"
PORT = 5050
ADDR = (SERVER_IP, PORT)
client.connect(ADDR)

def Chat():
    while True:
        message = 0
        if not message == "Exit":
            message = input("Type Your message below\n").encode("utf-8")
            client.send(message)
            answer = client.recv(2048).decode("utf-8")
            print(answer)
        else:
            break