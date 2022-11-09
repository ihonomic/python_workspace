import socket
import os
import subprocess

HEADER = 64  # bytes
FORMAT = "utf-8"
PORT = 5050
SERVER = "172.20.10.14"  # OR remote server
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"[CONNECTING] Client is connecting to {SERVER}")

try:
    client.connect(ADDR)
    print(f"[CONNECTED] Success")
except socket.error as error:
    print(f"[CONNECTION FAILED] {error}")


def send_string(message):
    message = message.encode(FORMAT)
    # message_len = len(message)
    # send_len = str(message_len).encode(FORMAT)
    # # # pad it to be 64 bytes long
    # send_len += b" " * (HEADER - len(send_len))
    # client.send(send_len)
    client.send(message)

    # Response from server
    while True:
        response = client.recv(2048).decode(FORMAT)
        print(f"[SERVER RESPONSE] {response}")


if __name__ == "__main__":
    send_string("3;0;1;28;0;7;5;0;")

