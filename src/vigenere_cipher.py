from src.defs import SYMBOLS_PL, AlgorithmMode

slen = len(SYMBOLS_PL)

def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def run_vigenere(msg: str, key: str, mode: AlgorithmMode) -> str:
    result = ''
    key = generate_key(msg, key)
    for i in range(len(msg)):
        symbol = msg[i]
        key_symbol = key[i % len(key)]
        if symbol in SYMBOLS_PL:
            ind = SYMBOLS_PL.find(symbol)
            ind_k = SYMBOLS_PL.find(key_symbol)
            result += SYMBOLS_PL[(ind + ind_k if mode == AlgorithmMode.Encryption else ind - ind_k) % slen]
        else:
            result += symbol
    return result

def vigenere_encrypt(message: str, key: str) -> str:
    return run_vigenere(message, key, AlgorithmMode.Encryption)

def vigenere_decrypt(cipher: str, key: str):
    return run_vigenere(cipher, key, AlgorithmMode.Decryption)

if __name__ == '__main__':
    message = "siema elo trzy dwa zero"
    secret_key = "elo"
    cipher = vigenere_encrypt(message, secret_key)
    print(cipher)
    print(vigenere_decrypt(cipher, secret_key))