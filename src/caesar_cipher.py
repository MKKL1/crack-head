import pyperclip

from src.defs import AlgorithmMode, SYMBOLS_PL

slen = len(SYMBOLS_PL)


def run_caesar(msg: str, key: int, mode: AlgorithmMode) -> str:
    """
    :param msg:
    :param key:
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
    return run_caesar(msg, key, AlgorithmMode.Decryption)


def encrypt_caesar(msg, key):
    res = run_caesar(msg, key, AlgorithmMode.Encryption)
    pyperclip.copy(res)
    return res


def crack_caesar(msg):
    for i in range(slen):
        print(f"Key={i} msg={decrypt_caesar(msg, i)}")

if __name__ == '__main__':
    run_caesar("siema", 5, AlgorithmMode.Decryption.Encryption)