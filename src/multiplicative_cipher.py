from src.caesar_cipher import SYMBOLS_PL
from src.crypto_math import get_mod_inverse

symb_len = len(SYMBOLS_PL)

def multiplicative_encrypt(message, key):
    encrypted = ''
    for symbol in message:
        index = SYMBOLS_PL.find(symbol)
        encrypted += SYMBOLS_PL[index * key % symb_len]
    return encrypted

def multiplicative_decrypt(message, key):
    decrypted = ''
    inv_key = get_mod_inverse(key, symb_len)
    for symbol in message:
        index = SYMBOLS_PL.find(symbol)
        decrypted += SYMBOLS_PL[index * inv_key % symb_len]
    return decrypted