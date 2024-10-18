import socket
import threading


def handle_client(conn, addr, clients):
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                print(f"Message from {addr}: {message}")
                # Client messages are not broadcasted to other clients.
            else:
                remove(conn, clients)
        except:
            continue


def broadcast(message, clients):
    """Broadcasts a message from the server to all connected clients."""
    for client in clients:
        try:
            client.send(message.encode())
        except:
            remove(client, clients)


def remove(connection, clients):
    """Remove a client from the list if connection is lost."""
    if connection in clients:
        clients.remove(connection)


def server_message(clients):
    """Allows the server admin to input and broadcast messages."""
    while True:
        message = input("Server: ")
        if message.strip():
            broadcast("Server: " + message, clients)


def main():
    host = '127.0.0.1'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    clients = []
    print("Server is running and listening...")

    # Start a thread for the server to send broadcast messages
    threading.Thread(target=server_message, args=(clients,)).start()

    while True:
        conn, addr = server_socket.accept()
        clients.append(conn)
        print(f"Connected to {addr}")
        # Start a new thread for each client connection
        threading.Thread(target=handle_client, args=(conn, addr, clients)).start()


if __name__ == '__main__':
    main()
