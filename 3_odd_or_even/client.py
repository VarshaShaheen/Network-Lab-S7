import socket

host = socket.gethostname()
port = 5003


def client_func():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input("Enter the message: ")
    client_sock.sendto(message.encode(), (host, port))
    data, addr = client_sock.recvfrom(1024)
    print(data.decode())
    client_sock.close()


if __name__ == '__main__':
    client_func()
