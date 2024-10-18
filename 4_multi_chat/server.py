import socket, threading


def clientX(c_soc, c_name):
    while True:
        mssg = c_soc.recv(1024).decode()
        print(f"{c_name}: {mssg}")
        tx(mssg, c_name)


def tx(mssg, c_name):
    for client in clients:
        if client[1] != c_name:
            client[0].send(f"{c_name}: {mssg}".encode())


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 8200))

server.listen(5)

clients = []

while True:
    c_soc, c_addr = server.accept()
    c_name = c_soc.recv(1024).decode()

    print(f"{c_name} connected !! ")
    c_soc.send("Connected!!!".encode())

    clients.append((c_soc, c_name))

    tx_thread = threading.Thread(target=clientX, args=(c_soc, c_name))
    tx_thread.start()
