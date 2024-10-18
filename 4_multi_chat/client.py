import socket
import threading

host = socket.gethostname()
port = 5004


def send_message(client_socket):
    while True:
        message = input("Enter the message to send: ")
        if message:
            client_socket.sendto(message.encode(), (host,port))


def receive_message(cl_socket):
    while True:
        message = cl_socket.recv(1024).decode()
        if message:
            print("Received from server: ", message)


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host,port))

    send_thread = threading.Thread(target=send_message, args=(client_socket,)).start()
    receive_thread = threading.Thread(target=receive_message, args=(client_socket, )).start()
