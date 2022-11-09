import datetime
import socket
import threading
import time

HEADER = 64  # bytes
FORMAT = "utf-8"
REREAD_ON_QUERY = True
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # Get local ip address

ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

FILE_PATH = input("Enter path to file >> linuxpath= ")
FILE_CONTENT = open(FILE_PATH, 'r').readlines()
FILE_CONTENT = list(map(lambda string: string.strip(), FILE_CONTENT))


def handle_client(conn, addr):
    """ Between individual client & server - Runs concurrently """
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        #   Wait to recieve information from the client (socket)
        recieved_message = conn.recv(HEADER).decode(FORMAT)
        if recieved_message:

            print(f"[{addr}] : {recieved_message}")

            start_time = time.time()
            # Re-read the content of file
            if REREAD_ON_QUERY:
                FILE_CONTENT = open(FILE_PATH, 'r').readlines()
                FILE_CONTENT = list(map(lambda string: string.strip(), FILE_CONTENT))  # Remove whitespace \n

            if recieved_message.strip() in FILE_CONTENT:
                conn.send("STRING EXISTS \n".encode(FORMAT))
            else:
                conn.send("STRING NOT FOUND \n".encode(FORMAT))

            end_time = time.time()
            processing_time = round(end_time - start_time, 2)
            timestamp = datetime.datetime.now().strftime("%b %d, %Y - %I:%M %p")

            #  Send debug log
            conn.send(f"[DEBUG LOG] "
                      f"\n sent={recieved_message} "
                      f"\n requesting IP={addr[0]} "
                      f"\n {processing_time=}ms "
                      f"\n {timestamp=}".encode(FORMAT))

    conn.close()


def start():
    print("[STARTING] server is starting...")

    # LIsten for new connections
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")

    while True:
        # (who connected, info)
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        # print(f" \n[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    start()
