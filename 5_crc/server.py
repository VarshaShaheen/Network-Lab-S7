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


if __name__ == "__main__":
    host = socket.gethostname()
    port = 5005
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((host, port))
    while True:
        data, addr = server_sock.recvfrom(1024)
        data, key = data.decode().split(',')
        error_data, addr2 = server_sock.recvfrom(1024)
        error_data, key2 = error_data.decode().split(',')
        reminder1 = divide_func(data,key)
        reminder2 = divide_func(error_data,key)
        check = '0'*(len(key)-1)
        if reminder1 == check:
            print("no error in:" ,data)
        else:
            print("error in: ",data)
        if reminder2 == check:
            print("no error in:", error_data)
        else:
            print("error in: ", error_data)

