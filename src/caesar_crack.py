SYMBOLS_PL = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWXYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwxyzźż1234567890 !?.'
slen = len(SYMBOLS_PL)


def crack_caesar(msg, key, mode):
    """
    :param mode: 0=decryption 1=encryption
    """
    result = ''
    for symbol in msg:
        if symbol in SYMBOLS_PL:
            ind = SYMBOLS_PL.find(symbol)
            result += SYMBOLS_PL[(ind + key if mode == 1 else ind - key) % slen]
        else:
            result += symbol
    return result


def decrypt_caesar(msg, key):
    return crack_caesar(msg, key, 0)


def encrypt_caesar(msg, key):
    return crack_caesar(msg, key, 1)
