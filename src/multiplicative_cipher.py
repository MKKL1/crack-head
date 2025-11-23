from src.caesar_cipher import SYMBOLS_PL
from src.crypto_math import get_mod_inverse,gcd


class MultiplicativeCipher:
    """Multiplicative cipher with configurable symbol set."""

    def __init__(self, symbols: str = SYMBOLS_PL):
        self.symbols = symbols
        self.length = len(symbols)

    def encrypt(self, message: str, key: int) -> str:
        """Encrypt message using multiplicative cipher."""
        if gcd(key, self.length) != 1:
            raise ValueError(f"Key {key} must be coprime with alphabet length {self.length}")

        encrypted = ''
        for symbol in message:
            if symbol in self.symbols:
                index = self.symbols.find(symbol)
                encrypted += self.symbols[(index * key) % self.length]
            else:
                encrypted += symbol
        return encrypted

    def decrypt(self, cipher: str, key: int) -> str:
        """Decrypt cipher using multiplicative cipher."""
        if gcd(key, self.length) != 1:
            raise ValueError(f"Key {key} must be coprime with alphabet length {self.length}")

        inv_key = get_mod_inverse(key, self.length)
        decrypted = ''
        for symbol in cipher:
            if symbol in self.symbols:
                index = self.symbols.find(symbol)
                decrypted += self.symbols[(index * inv_key) % self.length]
            else:
                decrypted += symbol
        return decrypted

if __name__ == '__main__':
    ceasar = MultiplicativeCipher()
    key = 23233
    msg = "siema elo"
    enc = ceasar.encrypt(msg, key)

    dec = ceasar.decrypt(enc, key)

    print("========Multiplicative cipher========")
    print(f"Encrypting message: '{msg}' with key: '{key}'")
    print(f"Encrypted message: '{enc}'")
    print(f"Decrypting: '{enc}' with key: '{key}'")
    print(f"Decrypted message: '{dec}'")