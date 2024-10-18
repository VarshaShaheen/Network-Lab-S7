def decrypt(cipher,key):
    arr = [['\n' for i in range(len(cipher))] for i in range(key)]

    go_down = False
    row = 0
    col = 0

    for letter in cipher:
        if row == 0:
            go_down = True
        if row == (key - 1):
            go_down = False

        arr[row][col] = '*'
        col += 1
        if go_down:
            row += 1
        else:
            row -= 1

    count = 0
    for i in range(key):
        for j in range(len(cipher)):
            if arr[i][j] == '*':
                arr[i][j] = cipher[count]
                count += 1

    print(arr)

    plaintext = ''
    go_down = False
    row = 0
    col = 0

    for i in range(len(cipher)):
        if row == 0:
            go_down = True
        if row == (key - 1):
            go_down = False

        plaintext += arr[row][col]
        col += 1
        if go_down:
            row += 1
        else:
            row -= 1

    return plaintext

if __name__ == '__main__':
    cipher = input("Enter the cipher: ")
    key = int(input("Enter the key: "))
    matrix = decrypt(cipher, key)
    print(matrix)