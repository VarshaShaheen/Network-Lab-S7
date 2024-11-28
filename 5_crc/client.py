import socket


def xor(a, b):
    result = ''
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'

    return result


def divide_func(a, b):
    pick = len(b)
    tmp = a[0:pick]

    while pick < len(a):
        if tmp[0] == '1':
            tmp = xor(tmp, b) + a[pick]
        else:
            tmp = xor('0' * pick, tmp) + a[pick]
        pick += 1

    if tmp[0] == 1:
        tmp = xor(tmp, b)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp


if __name__ == '__main__':
    host = socket.gethostname()
    port = 5005
    data = input("Enter the message: ")
    key = input("Enter the key: ")
    tmp = data + '0'*(len(key)-1)
    reminder = divide_func(tmp,key)
    print("reminder is: ",reminder)
    message = data + reminder
    print("The result without error is: ",message)
    error = divide_func(tmp,key.replace('1','0'))
    error_data = data + error
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.sendto(f'{message},{key}'.encode(), (host, port))
    print("The result with error is: ", error_data)
    client_sock.sendto(f'{error_data},{key}'.encode(), (host, port))
    client_sock.close()
