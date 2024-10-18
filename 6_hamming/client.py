import socket
import random

host = socket.gethostname()
port = 5006


def add_parity(message):
    a = [int(bit) for bit in message]
    p1 = a[0] ^ a[1] ^ a[3]
    p2 = a[0] ^ a[2] ^ a[3]
    p3 = a[1] ^ a[2] ^ a[3]
    message = str(p1) + str(p2) + str(a[0]) + str(p3) + str(a[1]) + str(a[2]) + str(a[3])
    return message


if __name__ == '__main__':
    message = input("Enter the 4 bit data: ")
    message = add_parity(message)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Message without error is: ", message)
    choice = int(input("Enter 1 for error and 0 for no error: "))
    if choice == 1:
        pos = random.randint(0,6)
        temp = list(message)
        print("Error inserted at position: ",pos)
        if temp[pos] == '1':
            temp[pos] = '0'
        else:
            temp[pos] = '1'
        message = ''.join(temp)
        print("Message with error is: ", message)
    client_socket.sendto(message.encode(), (host,port))
    client_socket.close()
