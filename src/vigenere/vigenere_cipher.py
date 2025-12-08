from src.defs import AlgorithmMode, SYMBOLS_PL


class VigenereCipher:
    """Vigenere cipher with configurable symbol set."""

    def __init__(self, symbols: str = SYMBOLS_PL):
        self.symbols = symbols
        self.modulus = len(symbols)

    def encrypt(self, message: str, key: str) -> str:
        return self._process(message, key, mode=AlgorithmMode.Encryption)

    def decrypt(self, cipher: str, key: str) -> str:
        return self._process(cipher, key, mode=AlgorithmMode.Decryption)

    def _process(self, text: str, key: str, mode: AlgorithmMode) -> str:
        result = []
        key_len = len(key)

        for i, char in enumerate(text):
            key_char = key[i % key_len]
            txt_idx = self.symbols.find(char)
            key_idx = self.symbols.find(key_char)

            if mode == AlgorithmMode.Encryption:
                new_idx = (txt_idx + key_idx) % self.modulus
            else:
                new_idx = (txt_idx - key_idx) % self.modulus

            result.append(self.symbols[new_idx])

        return "".join(result)

if __name__ == '__main__':
    message = "siema elo trzy dwa zero"
    secret_key = "elo"
    cipher = VigenereCipher()
    enc = cipher.encrypt(message, secret_key)
    print(enc)
    print(cipher.decrypt(enc, secret_key))