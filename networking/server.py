import socket
import threading

HEADER = 64  # bytes
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
# SERVER = "192.168.15.243" - where the server will run on. In this case, locally
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    """ Between individual client & server - Runs concurrently """
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        #   Wait to recieve information from the client (socket)
        recieved_message = conn.recv(HEADER).decode(FORMAT)
        if recieved_message:
            message_len = int(recieved_message)  # length of incoming
            message = conn.recv(message_len).decode(FORMAT)  # actual message
            if message == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] : {message}")
            conn.send("Message recieved".encode(FORMAT))

    conn.close()


def start():
    """ Handle new connections & distributes to where they need to go """
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        # (who connected, info)
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f" \n [ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")

start()
