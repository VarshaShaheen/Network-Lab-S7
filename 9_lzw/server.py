import socket
import json

host = socket.gethostname()
port = 5009


def get_key(data, value):
    for key, val in data.items():
        if value == str(val):
            return key
    return " "


def decrypt(cipher, data):
    plaintext = ""
    cipher = cipher.split('#')
    print(cipher)
    print(data)
    for l in cipher:
        plaintext += get_key(data, l)
    return plaintext


if __name__ == '__main__':
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((host, port))
    print("Server listening...")
    while True:
        packet, addr = server_sock.recvfrom(4096)
        data = json.loads(packet.decode())
        cipher = data['cipher']
        dict = data['dict']  # Receive dictionary sent from client

        plaintext = decrypt(cipher, dict)
        print("Decrypted text:", plaintext)
