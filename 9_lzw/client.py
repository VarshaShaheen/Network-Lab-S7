import socket
import json


host = socket.gethostname()
port = 5009

def compress(message):
    dict = {chr(i): i for i in range(256)}

    dict_size = 256
    cipher = ''
    w = ""
    cipher = ""


    for c in message:
        wc = w + c
        if wc in dict:
            w = wc
        else:
            cipher = cipher + str(dict[w]) + "#"
            dict[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        cipher += str(dict[w]) + '#'

    return cipher, dict


if __name__ == '__main__':
    message = input("Enter a message: ")
    cipher, dict = compress(message)
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data_to_send = json.dumps({'cipher': cipher, 'dict': dict})
    client_sock.sendto(data_to_send.encode(), (host, port))
    print("The cipher and dictionary have been sent to the server!")
    client_sock.close()
    client_sock.close()

