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
from src.crypto_math import get_mod_inverse,gcd

SYMBOLS_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,.'"


class AffineCipher:
    """Affine cipher with configurable symbol set."""

    def __init__(self, symbols: str = SYMBOLS_EN):
        self.symbols = symbols
        self.length = len(symbols)

    def encrypt(self, message: str, key: int) -> str:
        """Encrypt message using affine cipher."""
        key_a, key_b = self.get_key_parts(key)
        self.check_keys(key_a, key_b, AlgorithmMode.Encryption)

        cipher_text = ''
        for symbol in message:
            if symbol in self.symbols:
                symbol_index = self.symbols.find(symbol)
                cipher_text += self.symbols[(symbol_index * key_a + key_b) % self.length]
            else:
                cipher_text += symbol
        return cipher_text

    def decrypt(self, cipher: str, key: int) -> str:
        """Decrypt cipher using affine cipher."""
        key_a, key_b = self.get_key_parts(key)
        self.check_keys(key_a, key_b, AlgorithmMode.Decryption)

        plain_text = ''
        mod_inv_key_a = get_mod_inverse(key_a, self.length)

        for symbol in cipher:
            if symbol in self.symbols:
                symbol_index = self.symbols.find(symbol)
                plain_text += self.symbols[
                    ((symbol_index - key_b) * mod_inv_key_a) % self.length
                    ]
            else:
                plain_text += symbol
        return plain_text

    def get_key_parts(self, key: int) -> tuple[int, int]:
        """Split combined key into keyA and keyB."""
        key_a = key // self.length
        key_b = key % self.length
        return key_a, key_b

    def check_keys(self, key_a: int, key_b: int, mode: AlgorithmMode):
        """Validate key components."""
        if key_a == 1 and mode == AlgorithmMode.Encryption:
            raise ValueError('Cipher is weak when keyA=1. Choose different key.')
        if key_b == 0 and mode == AlgorithmMode.Encryption:
            raise ValueError('Cipher is weak when keyB=0. Choose different key.')
        if key_a < 0 or key_b < 0 or key_b >= self.length:
            raise ValueError('Both key parts must be positive and keyB < alphabet length')
        if gcd(key_a, self.length) != 1:
            raise ValueError(
                f'keyA must be coprime with alphabet length {self.length}'
            )

if __name__ == '__main__':
    affine = AffineCipher()
    key = 23233
    msg = "siema elo"
    enc = affine.encrypt(msg, key)

    dec = affine.decrypt(enc, key)

    print("========Affine cipher========")
    print(f"Encrypting message: '{msg}' with key: '{key}'")
    print(f"Encrypted message: '{enc}'")
    print(f"Decrypting: '{enc}' with key: '{key}'")
    print(f"Decrypted message: '{dec}'")