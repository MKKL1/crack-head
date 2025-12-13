import itertools
from operator import itemgetter
from src.frequency_analysis import FrequencyAnalyzer
from src.vigenere.vigenere_cipher import VigenereCipher


class BabbageCracker:
    def __init__(self):
        self.analyzer = FrequencyAnalyzer()
        # Re-use your Vigenere logic; it handles single-char keys automatically via modulo
        self.cipher = VigenereCipher(self.analyzer.SYMBOLS)

    def crack(self, ciphertext: str, key_length: int) -> list[tuple[str, str]]:
        """
        Attempts to crack Vigenere by treating it as interleaved Caesar ciphers.
        Returns a list of (key, decrypted_message).
        """
        ciphertext_up = ciphertext.upper()
        key_columns_options = []

        # 1. SOLVE EACH COLUMN INDEPENDENTLY
        for i in range(key_length):
            # Extract every Nth letter (Slicing is O(1) syntax, O(N) execution)
            # Logic: Start at i, jump by key_length
            sub_sequence = ciphertext_up[i::key_length]

            # Find the best single letters for this column
            best_letters = self._solve_single_caesar_column(sub_sequence)
            key_columns_options.append(best_letters)

        # 2. GENERATE AND TEST FULL KEYS
        results = []
        # Cartesian Product: Combine best options for Col 1, Col 2, etc.
        # e.g., Col1=['A'], Col2=['B', 'C'] -> "AB", "AC"
        for key_tuple in itertools.product(*key_columns_options):
            full_key = "".join(key_tuple)
            decrypted_text = self.cipher.decrypt(ciphertext_up, full_key)
            results.append((full_key, decrypted_text))

            # Optional: Print here if you want real-time output like the lab
            # print(f"Key: {full_key} | Msg: {decrypted_text[:50]}...")

        return results

    def _solve_single_caesar_column(self, sub_sequence: str) -> list[str]:
        """
        Brute-forces a single column (Caesar cipher) and returns the top scoring letters.
        Ref: Lab 5 [cite: 83-122]
        """
        scores = []

        # Try every letter A-Z as the key for this specific column
        for letter in self.analyzer.SYMBOLS:
            # Decrypt the slice using just this letter
            # (Our Vigenere class handles single-char keys by repeating them)
            decrypted_chunk = self.cipher.decrypt(sub_sequence, letter)

            # Score the English-ness (0-12 points)
            score = self.analyzer.get_english_frequency_match_score(decrypted_chunk)
            scores.append((letter, score))

        # Filter Logic from Lab:
        # 1. Sort by Score Descending
        scores.sort(key=itemgetter(1), reverse=True)

        # 2. Take Top 5 candidates (Arbitrary limit from instructions)
        top_candidates = scores[:5]

        # 3. Keep ONLY the ones tied for the absolute best score in that group
        #    (If best is 9, keep all 9s. Drop the 8s.)
        max_score = top_candidates[0][1]
        best_letters = [item[0] for item in top_candidates if item[1] == max_score]

        return best_letters


# --- Usage ---
if __name__ == "__main__":
    test_msg = 'PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'

    cracker = BabbageCracker()
    possible_solutions = cracker.crack(test_msg, key_length=4)

    print(f"\nFound {len(possible_solutions)} candidate(s):")
    for key, text in possible_solutions:
        print(f"Key: {key} -> {text}")