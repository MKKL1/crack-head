# import _cryptomath as cm
# import _multiplicativeCipher as mc
# import pyperclip, random, sys
#
# SYMBOLS_PL = mc.SYMBOLS_PL
# length = len(SYMBOLS_PL)
# mode = 0
#
#
# def main():
#     message_ = input('Wrpowadź treść wiadomości: ')
#     key_ = input('Wprowadź klucz dla szyfru afinicznego: ')
#     # musi to być liczba całkowita
#     # wygenerowana z niej zostanie część multiplikatywna keyA
#     # ..oraz część addytywna keyB
#     mode_ = input('Wybierz tryb pracy: 1=enkrypcja lub 0=dekrypcja: ')
#     mode = int(mode_)
#     outcome = ''
#
#     if mode == 1:
#         outcome = affineEncrypt(message_, int(key_))
#     elif mode == 0:
#         outcome = affineDecrypt(message_, int(key_))
#
#     print(outcome)
import sys

from src.crypto_math import gcd, get_mod_inverse
from src.defs import SYMBOLS_PL, AlgorithmMode

SYMBOLS_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,.'"
length = len(SYMBOLS_EN)

def getKeyParts(key):
    keyA = key // length
    keyB = key % length
    return keyA, keyB


def check_keys(keyA, keyB, mode: AlgorithmMode):
    if keyA == 1 and mode == 1:
        sys.exit('Szyfr jest słaby gdy keyA=1. Wybierz inny klucz. ')
    if keyB == 0 and mode == 1:
        sys.exit('Szyfr jest słaby gdy keyB=0. Wybierz inny klucz. ')
    if keyA < 0 or keyB < 0 or keyB >= length:
        sys.exit('Obie części klucz muszą być dodatnie...')
    if gcd(keyA, length) != 1:
        sys.exit('Część keyA musi być względnie pierwsza z długością alfabetu {0}'.format(length))


def affine_encrypt(message, key):
    keyA, keyB = getKeyParts(key)
    check_keys(keyA, keyB, AlgorithmMode.Encryption)
    cipherText = ''
    for symbol in message:
        if symbol in SYMBOLS_EN:
            symbolIndex = SYMBOLS_EN.find(symbol)
            cipherText += SYMBOLS_EN[(symbolIndex * keyA + keyB) % length]
        else:
            cipherText += symbol
    # pyperclip.copy(cipherText)
    return cipherText


def affine_decrypt(message, key):
    keyA, keyB = getKeyParts(key)
    check_keys(keyA, keyB, AlgorithmMode.Decryption)
    plainText = ''
    modMultiplicationInverseOfKeyA = get_mod_inverse(keyA, length)
    for symbol in message:
        if symbol in message:
            symbolIndex = SYMBOLS_EN.find(symbol)
            plainText += SYMBOLS_EN[((symbolIndex - keyB) * modMultiplicationInverseOfKeyA) % length]
        else:
            plainText += symbol
    return plainText
#
#
if __name__ == '__main__':
    k = 2323
    c = affine_encrypt("siemaelo", k)

    print(c)

    msg = affine_decrypt(c, k)

    print(msg)

