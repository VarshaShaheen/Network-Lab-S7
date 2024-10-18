import socket

host = socket.gethostname()
port = 5001


def client_func():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    data = input("Enter a meassage: ")
    client_socket.sendto(data.encode(), (host, port))
    message, addr = client_socket.recvfrom(1024)
    print("Received from server: ", message.decode())
    client_socket.close()


if __name__ == '__main__':
    client_func()
