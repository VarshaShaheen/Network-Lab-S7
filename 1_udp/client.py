import socket

host = socket.gethostname()
port = 5000


def client_func():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = input("Enter a message:")
    client_socket.sendto(data.encode(), (host, port))

    message, addr = client_socket.recvfrom(1024)
    print(message.decode())

    client_socket.close()


if __name__ == "__main__":
    client_func()
