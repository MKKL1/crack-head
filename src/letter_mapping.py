import re
from src.word_pattern import WordPattern
from src.subsitution_cipher import SubstitutionCipher

class SubstitutionCracker:
    def __init__(self):
        self.word_pattern = WordPattern()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def crack(self, message: str) -> (str,str):
        cipher_words = set(re.sub(r'[^A-Z\s]', '', message.upper()).split())
        mapping = self._build_intersected_mapping(cipher_words)
        final_mapping = self._cleanup_mapping(mapping)
        return self._decrypt_message(message, final_mapping), self._generate_key_string(final_mapping)

    def _build_intersected_mapping(self, cipher_words: set[str]) -> dict[str, set[str]]:
        mapping = {}

        for word in cipher_words:
            pattern = self.word_pattern.get_word_pattern(word)
            candidates = self.word_pattern.get_words_from_pattern(pattern)

            if not candidates:
                continue

            word_knowledge = {}
            for cand in candidates:
                for i in range(len(word)):
                    cipher_char = word[i]
                    plain_char = cand[i]

                    if cipher_char not in word_knowledge:
                        word_knowledge[cipher_char] = set()

                    word_knowledge[cipher_char].add(plain_char)

            for char, possible_plain_chars in word_knowledge.items():
                if char not in mapping:
                    mapping[char] = possible_plain_chars
                else:
                    mapping[char] &= possible_plain_chars

        return mapping

    def _cleanup_mapping(self, mapping: dict[str, set[str]]) -> dict[str, set[str]]:
        to_process = []
        for char, possibilities in mapping.items():
            if len(possibilities) == 1:
                solved_letter = list(possibilities)[0]
                to_process.append(solved_letter)

        while to_process:
            to_remove = to_process.pop(0)
            for cipher_char, possibilities in mapping.items():
                if len(possibilities) == 1:
                    continue

                if to_remove in possibilities:
                    possibilities.remove(to_remove)

                    if len(possibilities) == 1:
                        to_process.append(list(possibilities)[0])

        return mapping

    def _decrypt_message(self, message: str, mapping: dict[str, set[str]]) -> str:
        solved_key = {}
        for cipher_char, possibilities in mapping.items():
            if len(possibilities) == 1:
                solved_key[cipher_char] = list(possibilities)[0]

        result = []
        for char in message:
            upper_char = char.upper()

            if not upper_char.isalpha():
                result.append(char)
                continue

            if upper_char in solved_key:
                decrypted_char = solved_key[upper_char]
                if char.islower():
                    result.append(decrypted_char.lower())
                else:
                    result.append(decrypted_char)

            else:
                result.append('_')

        return "".join(result)

    def _generate_key_string(self, mapping: dict[str, set[str]]) -> str:
        plain_to_cipher = {}
        for cipher_char, possibilities in mapping.items():
            if len(possibilities) == 1:
                plain_char = next(iter(possibilities))
                plain_to_cipher[plain_char] = cipher_char

        key_chars = []
        for plain_char in self.alphabet:
            key_chars.append(plain_to_cipher.get(plain_char, '_'))

        return "".join(key_chars)


if __name__ == '__main__':
    msg = "Perpendicular reconstruction"
    # msg = "Perpendicular reconstruction That is a great challenge. The most viewed solution on LeetCode is rarely the one with the most advanced Python syntax. It is usually the one that is easiest to read and easiest to verify mentally. However, there is a catch: sometimes a cipher text is too short to solve every single letter perfectly. You might end up with a few letters that still have 2 possibilities. If your loop only stops when everything is solved, it might run forever in those cases! A safer approach is to stop looping when we stop making progress. If we go through the whole list and don't remove a single letter, running the loop again won't help."
    cipher = SubstitutionCipher()


    key = cipher.get_random_key()
    enc = cipher.encrypt(msg, key)

    print(f"Original:      {msg}")
    print("-" * 50)
    print(f"Key used:      {key}")
    print(f"Encrypted:     {enc}")

    cracker = SubstitutionCracker()
    decrypted = cracker.crack(enc)

    print("-" * 50)
    print(f"Recovered key: {decrypted[1]}")
    print(f"Decrypted:     {decrypted[0]}")
