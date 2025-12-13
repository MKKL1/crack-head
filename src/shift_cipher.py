import math
from typing import List, Dict, Any
from src.detect_english import EnglishDetector


class TranspositionCipher:
    """
    Implements Columnar Transposition Cipher logic.
    Ref: Shifts characters into a grid based on the key (column count).
    """

    def encrypt(self, message: str, key: int) -> str:
        """
        Encrypts message by writing to 'key' columns and reading rows.
        """
        # Create a list of strings for each column
        columns = [''] * key

        for i, char in enumerate(message):
            col_index = i % key
            columns[col_index] += char

        return ''.join(columns)

    def decrypt(self, cipher: str, key: int) -> str:
        cols = key
        rows = math.ceil(len(cipher) / cols)
        empty_cells = (rows * cols) - len(cipher)

        columns = []
        position = 0

        for col_num in range(cols):
            is_short_column = col_num >= cols - empty_cells

            if is_short_column:
                height = rows - 1
            else:
                height = rows

            column_text = cipher[position: position + height]
            columns.append(column_text)
            position += height

        result = []

        for row_num in range(rows):
            for column in columns:
                if row_num < len(column):
                    result.append(column[row_num])

        return ''.join(result)


class TranspositionHacker:
    """
    Tools to brute-force break the Transposition Cipher.
    """

    def __init__(self):
        self.cipher_engine = TranspositionCipher()
        self.detector = EnglishDetector()

    def hack(self, ciphertext: str) -> List[Dict[str, Any]]:
        """
        Smart brute-force: Tries keys and returns only English-like results.
        """
        candidates = []
        # Key limit: Theoretically up to length of message, but usually much smaller.
        # We check up to half the length as a reasonable heuristic.
        max_key = len(ciphertext) // 2

        for key in range(1, max_key + 1):
            decrypted_text = self.cipher_engine.decrypt(ciphertext, key)

            # Only keep candidates that look like valid English
            if self.detector.is_eng(decrypted_text):
                candidates.append({
                    "key": key,
                    "text": decrypted_text
                })

        return candidates


if __name__ == '__main__':
    # --- 1. Test the Cipher Logic ---
    cipher_tool = TranspositionCipher()
    secret_key = 3
    message = "HELLO WORLD"

    encrypted = cipher_tool.encrypt(message, secret_key)
    decrypted = cipher_tool.decrypt(encrypted, secret_key)

    print("======== TRANSPOSITION CIPHER ========")
    print(f"Original:  '{message}'")
    print(f"Encrypted: '{encrypted}'")
    print(f"Decrypted: '{decrypted}'")

    # --- 2. Test the Hacker Logic ---
    print("\n======== HACKER MODE ========")
    hacker = TranspositionHacker()

    # Let's try to hack the message we just encrypted
    results = hacker.hack(encrypted)

    for res in results:
        print(f"[CANDIDATE] Key: {res['key']} | Text: {res['text'][:40]}...")