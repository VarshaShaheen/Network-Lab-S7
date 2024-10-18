import socket

host = socket.gethostname()
port = 5001


def server_func():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening at port: ", port)

    while True:
        conn, addr = server_socket.accept()
        print("connected by:", addr)
        while True:
            data = conn.recv(1024)
            message = data.decode().upper()
            conn.send(message.encode())


if __name__ == '__main__':
    server_func()
