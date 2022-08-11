import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_IP = "192.168.1.61"
PORT = 5050
ADDR = (SERVER_IP, PORT)
server.bind(ADDR)

server.listen()

def client_handler(conn, addr):
    global answer
    message = conn.recv(2048).decode("utf-8")
    print(message)
    answer = input("Type Your message below\n:").encode("utf-8")
    conn.send(answer)



def chat():
    while True:
            if answer == "Exit":
                break
            print('waiting')
            conn, addr = server.accept()
            client_handler(conn, addr)
            
