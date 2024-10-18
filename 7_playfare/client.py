import socket

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z']


def search(matrix, key):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == key:
                return i, j


def modify_text(message):
    if len(message) % 2 != 0:
        message += 'x'
    plaintext = ''
    for i in range(0, len(message), 2):
        if message[i] == message[i + 1]:
            plaintext += message[i]
            plaintext += 'x'
            plaintext += message[i + 1]
            plaintext += 'x'
        else:
            plaintext += message[i]
            plaintext += message[i + 1]
    return plaintext


def make_digraph(message):
    digraph = []
    for i in range(2, len(message), 2):
        digraph.append(message[i - 2:i])

    digraph.append(message[len(message) - 2:len(message)])
    return digraph


def make_matrix(key):
    matrix = []
    row = []
    key_letters = []
    count = 0
    for letter in key:
        if letter not in key_letters:
            key_letters.append(letter)

    for letter in key_letters:
        row.append(letter)
        count += 1
        if count == 5:
            matrix.append(row)
            row = []
            count = 0
    for letter in list1:
        if letter not in key:
            row.append(letter)
            count += 1
        if count == 5:
            matrix.append(row)
            row = []
            count = 0
    return matrix


def encrypt(matrix, digraph):
    cipher = ''
    for couple in digraph:
        row1, col1 = search(matrix, couple[0])
        row2, col2 = search(matrix, couple[1])
        if row1 == row2:
            cipher += matrix[row1][((col1+1) % 5)]
            cipher += matrix[row1][((col2+1) % 5)]
        elif col1 ==  col2 :
            cipher += matrix[(row1+1)%5][col1]
            cipher += matrix[(row2 + 1) % 5][col1]
        else:
            cipher += matrix[row1][col2]
            cipher += matrix[row2][col1]
    return cipher


if __name__ == '__main__':
    message = input("Enter the message: ")
    key = input("Enter the key: ")
    message = modify_text(message)
    digraph = make_digraph(message)
    matrix = make_matrix(key)
    cipher = encrypt(matrix, digraph)

    print(digraph)
    print(matrix)
    print(cipher)
