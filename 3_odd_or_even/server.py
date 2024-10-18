import socket

host = socket.gethostname()
port = 5003


def server_func():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((host, port))
    print("Sever listening at port: ", port)

    while True:
        data, addr = server_sock.recvfrom(1024)
        data = int(data.decode())
        if data % 2 == 0:
            message = "even"
            server_sock.sendto(message.encode(), addr)
        else:
            message = "odd"
            server_sock.sendto(message.encode(), addr)


if __name__ == '__main__':
    server_func()
