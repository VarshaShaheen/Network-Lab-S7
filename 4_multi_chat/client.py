import socket
import threading


def receive_message(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            print(message)
        except:
            print("You have been disconnected from the server.")
            sock.close()
            break


def send_message(sock):
    while True:
        message = input('')
        sock.send(message.encode())


def main():
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    threading.Thread(target=receive_message, args=(client_socket,)).start()
    threading.Thread(target=send_message, args=(client_socket,)).start()


if __name__ == '__main__':
    main()
