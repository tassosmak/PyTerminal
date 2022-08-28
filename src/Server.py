import socket




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
SERVER_IP = socket.gethostbyname(hostname)
PORT = 5050
ADDR = (SERVER_IP, PORT)
server.bind(ADDR)
SendOnly = False
Say = 0

server.listen()

def client_handler(conn, addr, Say, SendOnly=False):
    global answer
    if SendOnly:
        answer = Say
        conn.send(answer)
    else:
        message = conn.recv(2048).decode("utf-8")
        print(message)
        answer = input("Type Your message below\n:").encode("utf-8")
        conn.send(answer)



def chat(SendOnly, Say):
    while True:        
            print('waiting')
            conn, addr = server.accept()
            client_handler(conn, addr, SendOnly, Say)
            if client_handler.answer == "Exit":
                break
            
def SendOnly(Say):
    client_handler()