import socket
import json

host = socket.gethostname()
port = 5000


def server_func():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("server listening at port: ", port)

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        print("Received message: ", message)
        message = message.upper()
        server_socket.sendto(message.encode(), addr)


if __name__ == '__main__':
    server_func()
