import socket,threading

def rx():
    while True:
        message = client.recv(1024).decode()
        print(message)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 8200))

name = input("username: ")
client.send(name.encode())
print(client.recv(1024).decode())

rx_thread = threading.Thread(target=rx)
rx_thread.start()

while True:
    message = input("")
    client.send(message.encode())
    if message == "exit":
        break

client.close()