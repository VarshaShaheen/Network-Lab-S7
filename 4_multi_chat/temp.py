import socket
import threading

host = socket.gethostname()
port = 11112


def broadcast(message, clients):
    for client in clients:
        client.send(message.encode())


def handleClient(conn, addr):
    while True:
        message = conn.recv(1024).decode()
        if message:
            print(f"Message from {addr}: {message}")


def sendMessage(clients):
    message = input("Enter the message to send: ")
    if message:
        broadcast(message, clients)


if __name__ == '__main__':
    clients = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    send_message_thread = threading.Thread(target=sendMessage, args=(clients,)).start()

    while True:
        client, addr = server_socket.accept()
        clients.append(client)
        print(f"Connected to {addr}")
        handleClient_thread = threading.Thread(target=handleClient, args=(client, addr)).start()

