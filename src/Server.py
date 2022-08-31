import socket




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
SERVER_IP = socket.gethostbyname(hostname)
PORT = 5050
ADDR = (SERVER_IP, PORT)
server.bind(ADDR)


server.listen()

def client_handler(conn, addr, No_recv, Send):
    global answer
    if No_recv:
        conn.send("Server")
        conn.send(Send)
    else:
        message = conn.recv(2048).decode("utf-8")
        print(message)
        answer = input("Type Your message below\n:").encode("utf-8")
        conn.send(answer)



def chat():
    while True:        
            print('waiting')
            conn, addr = server.accept()
            client_handler(conn, addr)
            if client_handler.answer == "Exit":
                break
            
def SendOnly(Say):
    while True:
        conn, addr = server.accept()
        client_handler(conn, addr, No_recv=True, Send=Say)