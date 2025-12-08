from src.vigenere.vigenere_cipher import VigenereCipher
from src.detect_english import EnglishDetector


class VigenereDictionaryCracker:
    def __init__(self, dictionary_path: str):
        self.cipher_engine = VigenereCipher()
        self.english_detector = EnglishDetector()
        self.dictionary = self._load_dictionary(dictionary_path)

    def solve(self, ciphertext: str) -> str | None:
        for word in self.dictionary:
            potential_plaintext = self.cipher_engine.decrypt(ciphertext, word)

            if self.english_detector.is_eng(potential_plaintext, 80):
                print(f"\nPossible match found at key={word} text={potential_plaintext[:100]}")
                response = input("Is this the correct message? (Y/n): ").strip().upper()
                if response == 'Y':
                    return potential_plaintext

        print("failure")
        return None

    def _load_dictionary(self, path: str) -> list[str]:
        try:
            with open(path, 'r') as f:
                return [line.strip().upper() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: Dictionary not found at {path}")
            return []


if __name__ == "__main__":
    cracker = VigenereDictionaryCracker("../../dictionary.txt")

    msg = "HELLO WORLD"
    secret = "KEY"
    cipher = VigenereCipher()
    encrypted = cipher.encrypt(msg, secret)

    result = cracker.solve(encrypted)

    if result:
        print(f"\nFinal Decrypted Message:\n{result}")