import socket
import random

host = socket.gethostname()
port = 5006


def check_parity(message):
    a = [int(bit) for bit in message]
    s1 = a[0] ^ a[2] ^ a[4] ^ a[6]
    s2 = a[1] ^ a[2] ^ a[5] ^ a[6]
    s4 = a[3] ^ a[4] ^ a[5] ^ a[6]
    error_pos = (s1 * 1) + (s2 * 2) + (s4 * 4)
    print(error_pos-1)
    if error_pos > 0:
        print("Error found at position: ", error_pos-1)
        a[error_pos-1] ^= 1
        print("Corrected string is: ", ''.join(str(bit) for bit in a))


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    while True:
        message, addr = server_socket.recvfrom(1024)
        message = message.decode()
        check_parity(message)
