import socket
import threading

host = socket.gethostname()
port = 5004


def send_func(client_socket):
    while True:
        message = input("Enter a message: ")
        if message:
            client_socket.sendto(message.encode(), (host, port))


def receive_func(client_socket):
    while True:
        message, addr = client_socket.recvfrom(1024)
        if message:
            print("received from server" + message.decode())


if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    send_thread = threading.Thread(target=send_func, args=(client_socket,)).start()
    receive_thread = threading.Thread(target=receive_func, args=(client_socket,)).start()
