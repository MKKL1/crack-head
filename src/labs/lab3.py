import pyperclip

from src.caesar_cipher import SYMBOLS_PL
from src.crypto_math import gcd
from src.multiplicative_cipher import multiplicative_encrypt, multiplicative_decrypt

symb_len = len(SYMBOLS_PL)

if __name__ == "__main__":
    print('Multiplicative Cipher d-_-b')
    message = input('message: ')
    key = input(f'key {symb_len}: ')

    while gcd(int(key), symb_len) != 1:
        print('Niepoprawny klucz')
        key = input(f'key {symb_len}')

    mode = input('1 enkrypcja, 2 dekrypcja: ')

    if mode == '1':
        outcome = multiplicative_encrypt(message, int(key))
    elif mode == '2':
        outcome = multiplicative_decrypt(message, int(key))
    else:
        exit(1)
    pyperclip.copy(outcome)

    print("Wynik:", outcome)