def create_matrix(plaintext, key):
    arr = [['\n' for i in range(len(plaintext))] for j in range(key)]

    go_down = False
    row = 0
    col = 0

    for letter in plaintext:
        if row == 0:
            go_down = True
        if row == (key - 1):
            go_down = False

        arr[row][col] = letter
        col += 1
        if go_down:
            row += 1
        else:
            row -= 1
    print(arr)
    return arr


def encrypt(arr, plaintext, key):
    cipher = ''
    for i in range(key):
        for j in range(len(plaintext)):
            if arr[i][j] != '\n':
                cipher += arr[i][j]
    return cipher


if __name__ == '__main__':
    plaintext = input("Enter the message: ")
    key = int(input("Enter the key: "))
    matrix = create_matrix(plaintext, key)
    cipher = encrypt(matrix, plaintext, key)
    print(cipher)
