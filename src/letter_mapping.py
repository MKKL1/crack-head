import string

class SimpleSubstitutionMapper:
    def __init__(self, symbols: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self.symbols = symbols
        self.length = len(symbols)

    def get_blank_cipherletter_mapping(self) -> dict[str, list[str]]:
        return {char: [] for char in self.symbols}

    def add_letters_to_mapping(self, letter_mapping: dict, cipher_word: str, candidate: str) -> dict:
        cipher_word = cipher_word.upper()
        candidate = candidate.upper()

        for cipher_char, plain_char in zip(cipher_word, candidate):
            if cipher_char in letter_mapping:
                if plain_char not in letter_mapping[cipher_char]:
                    letter_mapping[cipher_char].append(plain_char)

        return letter_mapping

    def get_quasi_intersected_mappings(self, map_a: dict, map_b: dict) -> dict:
        intersected_mapping = self.get_blank_cipherletter_mapping()

        for letter in string.ascii_uppercase:
            list_a = map_a.get(letter, [])
            list_b = map_b.get(letter, [])

            if not list_a or not list_b:
                combined = list(set(list_a + list_b))
                intersected_mapping[letter] = combined
            else:
                intersection = [char for char in list_a if char in list_b]
                intersected_mapping[letter] = intersection

        return intersected_mapping


if __name__ == '__main__':
    mapper = SimpleSubstitutionMapper()

    mapping_empty = mapper.get_blank_cipherletter_mapping()

    cipher_word = "HGHF"
    candidate_1 = "THAT"

    map_from_word1 = mapper.get_blank_cipherletter_mapping()
    mapper.add_letters_to_mapping(map_from_word1, cipher_word, candidate_1)

    candidate_2 = "HIGH"
    map_from_word2 = mapper.get_blank_cipherletter_mapping()
    mapper.add_letters_to_mapping(map_from_word2, cipher_word, candidate_2)

    final_map = mapper.get_quasi_intersected_mappings(map_from_word1, map_from_word2)