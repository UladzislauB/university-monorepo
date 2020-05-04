import tables


def to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def from_bits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def apply_permutation(array, permutation):
    result = []
    for p in permutation:
        result.append(array[p - 1])
    return result


# input: key = 56 bits
# output: key = 64 bits
def get_extended_key(key):
    result = []
    sum = 0
    for i in range(56):
        result.append(key[i])
        sum += key[i]
        if (i + 1) in [7, 14, 21, 28, 35, 42, 49, 56]:
            result.append(int(sum % 2))
            sum = 0
    return result


# input: key = 56 bits
# output: keys[ {48 bits} ], len = 16 
def get_keys(key):
    extended_key = get_extended_key(key)
    result = []
    C = [apply_permutation(extended_key, tables.C0)]
    D = [apply_permutation(extended_key, tables.D0)]
    for i in range(16):
        C.append(C[i].copy())
        D.append(D[i].copy())
        for _ in range(tables.I[i]):
            C[i + 1].append(C[i + 1].pop(0))
            D[i + 1].append(D[i + 1].pop(0))
        new_key = apply_permutation(C[i + 1] + D[i + 1], tables.K)
        result.append(new_key)
    return result


# input: string = 8 chars, key = 7 chars
# output: string = 8 chars
def encrypt_block(string, key):
    keys = get_keys(to_bits(key))
    T0 = apply_permutation(to_bits(string), tables.IP)
    L = [T0[:32]]
    R = [T0[32:]]
    for i in range(1, 17):
        # L
        L.append(R[i - 1])

        # f1
        _F1 = apply_permutation(R[i - 1], tables.E)
        # f2
        _F2 = []
        for j in range(48):
            _F2.append((_F1[j] + keys[i - 1][j]) % 2)
        # f3
        _F3 = []
        for j in range(8):
            B = _F2[j * 6:(j + 1) * 6]
            a = B[0] * 2 + B[5]
            b = B[1] * 2 ** 3 + B[2] * 2 ** 2 + B[3] * 2 + B[4]
            _F3 += tables.BIN[tables.S[j][a][b]]
        # f4
        _F4 = apply_permutation(_F3, tables.P)

        # R
        R.append([])
        for j in range(32):
            R[i].append((L[i - 1][j] + _F4[j]) % 2)

    bits_result = apply_permutation(L[16] + R[16], tables.IP_)
    return from_bits(bits_result)


# input: string = 8 chars, key = 7 chars
# output: string = 8 chars
def decrypt_block(string, key):
    keys = get_keys(to_bits(key))
    T0 = apply_permutation(to_bits(string), tables.IP)
    L = [T0[:32]]
    R = [T0[32:]]
    for i in range(1, 17):
        # R
        R.append(L[i - 1])

        # f1
        _F1 = apply_permutation(L[i - 1], tables.E)
        # f2
        _F2 = []
        for j in range(48):
            _F2.append((_F1[j] + keys[15 - (i - 1)][j]) % 2)
        # f3
        _F3 = []
        for j in range(8):
            B = _F2[j * 6:(j + 1) * 6]
            a = B[0] * 2 + B[5]
            b = B[1] * 2 ** 3 + B[2] * 2 ** 2 + B[3] * 2 + B[4]
            _F3 += tables.BIN[tables.S[j][a][b]]
        # f4
        _F4 = apply_permutation(_F3, tables.P)

        # L
        L.append([])
        for j in range(32):
            L[i].append((R[i - 1][j] + _F4[j]) % 2)

    bits_result = apply_permutation(L[16] + R[16], tables.IP_)
    return from_bits(bits_result)


def encrypt(string, key):
    key = key[:7]
    while len(string) % 8 != 0:
        string += ' '
    result = ""
    for i in range(int(len(string) / 8)):
        result += encrypt_block(string[i * 8:(i + 1) * 8], key)
    return result


def decrypt(string, key):
    key = key[:7]
    while len(string) % 8 != 0:
        string += ' '
    result = ""
    for i in range(int(len(string) / 8)):
        result += decrypt_block(string[i * 8:(i + 1) * 8], key)
    return result
