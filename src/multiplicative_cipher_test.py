import math

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols_len = len(SYMBOLS)

def encrypt(msg: str, key: int) -> str:
    if math.gcd(key, symbols_len) != 1:
        raise ValueError("Invalid key")

    return _run(msg, key)

def decrypt(msg: str, key: int) -> str:
    decrypt_key = pow(key, -1, symbols_len)
    return _run(msg, decrypt_key)


def _run(msg: str, key: int) -> str:
    res = []
    for c in msg:
        enc_c = (SYMBOLS.find(c) * key) % symbols_len
        res.append(SYMBOLS[enc_c])

    return ''.join(res)

if __name__ == '__main__':
    msg = "SIEMAELO"
    enc = encrypt(msg, 3)
    print(enc)

    dec = decrypt(enc, 3)
    print(dec)