from src.defs import SYMBOLS_PL, AlgorithmMode


class VigenereCipher:
    """Vigenere cipher with configurable symbol set."""

    def __init__(self, symbols: str = SYMBOLS_PL):
        self.symbols = symbols
        self.length = len(symbols)

    def encrypt(self, message: str, key: str) -> str:
        """Encrypt message using Vigenere cipher."""
        return self._run(message, key, AlgorithmMode.Encryption)

    def decrypt(self, cipher: str, key: str) -> str:
        """Decrypt cipher using Vigenere cipher."""
        return self._run(cipher, key, AlgorithmMode.Decryption)

    def _run(self, text: str, key: str, mode: AlgorithmMode) -> str:
        """Core Vigenere cipher logic."""
        result = ''
        key_extended = self._generate_key(text, key)

        for i, symbol in enumerate(text):
            key_symbol = key_extended[i]
            if symbol in self.symbols:
                symbol_index = self.symbols.find(symbol)
                key_index = self.symbols.find(key_symbol)

                if mode == AlgorithmMode.Encryption:
                    new_index = (symbol_index + key_index) % self.length
                else:
                    new_index = (symbol_index - key_index) % self.length

                result += self.symbols[new_index]
            else:
                result += symbol
        return result

    def _generate_key(self, message: str, key: str) -> str:
        """Extend key to match message length."""
        if len(message) <= len(key):
            return key

        extended_key = list(key)
        for i in range(len(message) - len(key)):
            extended_key.append(key[i % len(key)])
        return "".join(extended_key)

if __name__ == '__main__':
    message = "siema elo trzy dwa zero"
    secret_key = "elo"
    cipher = vigenere_encrypt(message, secret_key)
    print(cipher)
    print(vigenere_decrypt(cipher, secret_key))