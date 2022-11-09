import socket
import threading

HEADER = 64  # bytes
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = "192.168.15.243"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(message):
    message = message.encode(FORMAT)
    message_len = len(message)
    send_len = str(message_len).encode(FORMAT)
    # pad it to be 64 bytes long
    send_len += b" " * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)

    # Response from server
    res = client.recv(2048).decode(FORMAT)
    print(f"[SERVER RESPONSE] {res}")


send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Ihon!")

send(DISCONNECT_MESSAGE)