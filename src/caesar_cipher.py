from src.defs import AlgorithmMode, SYMBOLS_PL

class CaesarCipher:
    """Caesar cipher with configurable symbol set."""

    def __init__(self, symbols: str = SYMBOLS_PL):
        self.symbols = symbols
        self.length = len(symbols)

    def encrypt(self, message: str, key: int) -> str:
        """Encrypt message using Caesar cipher."""
        return self._run(message, key, AlgorithmMode.Encryption)

    def decrypt(self, cipher: str, key: int) -> str:
        """Decrypt cipher using Caesar cipher."""
        return self._run(cipher, key, AlgorithmMode.Decryption)

    def _run(self, text: str, key: int, mode: AlgorithmMode) -> str:
        """Core Caesar cipher logic."""
        result = ''
        for symbol in text:
            if symbol in self.symbols:
                index = self.symbols.find(symbol)
                if mode == AlgorithmMode.Encryption:
                    result += self.symbols[(index + key) % self.length]
                else:
                    result += self.symbols[(index - key) % self.length]
            else:
                result += symbol
        return result

    def crack(self, cipher: str) -> list[tuple[int, str]]:
        """Brute force crack by trying all possible keys."""
        results = []
        for key in range(self.length):
            decrypted = self.decrypt(cipher, key)
            results.append((key, decrypted))
        return results

if __name__ == '__main__':
    ceasar = CaesarCipher()
    key = 23233
    msg = "siema elo"
    enc = ceasar.encrypt(msg, key)

    dec = ceasar.decrypt(enc, key)

    print("========Caesar cipher========")
    print(f"Encrypting message: '{msg}' with key: '{key}'")
    print(f"Encrypted message: '{enc}'")
    print(f"Decrypting: '{enc}' with key: '{key}'")
    print(f"Decrypted message: '{dec}'")