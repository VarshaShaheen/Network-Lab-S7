def determine_r(msg):
    r = 0
    while 2 ** r < len(msg) + 1 + r:
        r += 1
    print(r)
    return r


def create_hamming_set(m,r):
    temp = 0
    hamming_set = []
    for i in range(1,len(m)+r+1):
        if i == 2**temp :
            hamming_set.insert(0,0)
            temp += 1
        else:
            hamming_set.insert(0,int(m[-1]))
            m = m[:-1]
    print(hamming_set)
    return hamming_set

def hamming():
    message = input("Enter the message")
    msg = list(message)
    r = determine_r(msg)
    hamming_set = create_hamming_set(msg,r)
    for i in range(0,r+1):
        for j in range(2**i+1,len(hamming_set)+1):
            if j & (2**i) == 2**i :
                hamming_set[-1*(2**i)] = hamming_set[-1*(2**i)] ^ hamming_set[-j]
    print(hamming_set)


if __name__ == "__main__":
    hamming()
