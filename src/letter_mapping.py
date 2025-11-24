import re
import string

from src.subsitution_cipher import SubstitutionCipher
from src.word_pattern import WordPattern


class SimpleSubstitutionMapper:
    def __init__(self, symbols: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self.symbols = symbols
        self.length = len(symbols)

    def get_blank(self) -> dict[str, set[str]]:
        return {char: set() for char in self.symbols}

    def add_to_mapping(self, letter_mapping: dict[str, set[str]], cipher_word: str, candidate: str) -> dict[str, set[str]]:
        cipher_word = cipher_word.upper()
        candidate = candidate.upper()

        for cipher_char, plain_char in zip(cipher_word, candidate):
            if cipher_char in letter_mapping:
                if plain_char not in letter_mapping[cipher_char]:
                    letter_mapping[cipher_char].add(plain_char)

        return letter_mapping

    def get_quasi_intersected_mappings(self, map_a: dict, map_b: dict) -> dict:
        intersected_mapping = self.get_blank()

        for letter in self.symbols:
            set_a = set(map_a[letter])
            set_b = set(map_b[letter])
            if set_a == set() or set_b == set():
                intersected_mapping[letter] = set_a | set_b
            else:
                intersected_mapping[letter] = set_a & set_b

        return intersected_mapping

    def make_mapping(self, cipher_word: str, candidate: str):
        m = self.get_blank()
        self.add_to_mapping(m, cipher_word, candidate)

        return m

    def create_final_mapping(self, cipher_words: list[str], word_pattern: WordPattern):
        imappings = self.get_blank()
        for word in cipher_words:
            patern = word_pattern.get_word_pattern(word)
            candidates = word_pattern.get_words_from_pattern(patern)
            word_mapping = self.get_blank()

            for c in candidates:
                updated_word_mapping = self.add_to_mapping(word_mapping, word, c)
                word_mapping = updated_word_mapping

            imappings = self.get_quasi_intersected_mappings(imappings, word_mapping)
        return imappings

    def remove_solved_letters_from_mapping(self, map_: dict[str, set[str]]):
        loopAgain = True

        servedSolvedLetters = []
        while loopAgain:
            unservedSolvedLetters = list(filter(lambda k: len(map_[k]) == 1 and k not in servedSolvedLetters,map_))

            if not unservedSolvedLetters:
                loopAgain = False
            else:
                solvedLetter = unservedSolvedLetters[0]
                respectiveLetter = map_[solvedLetter][0]
                for key in map_:
                    if (respectiveLetter in map_[key]) and (key != solvedLetter):
                        map_[key].remove(respectiveLetter)
                servedSolvedLetters.append(solvedLetter)
        return map_


import re
nonletter = re.compile('[^A-Z\\s]')
def crack(message):
    #odszyfrowanie wiadomosci od tubylcow na kolowkium
    mapper = SimpleSubstitutionMapper()
    wp = WordPattern()
    intersectedMap = mapper.get_blank()
    cipher_word_list = nonletter.sub('', message.upper()).split()

    for n_word in cipher_word_list:
        pattern = wp.get_word_pattern(n_word)
        candidates = wp.get_words_from_pattern(pattern)
        initial_map = mapper.get_blank()
        for candidate in candidates:
            candidate_map = mapper.add_to_mapping(initial_map, n_word, candidate)
            initial_map = candidate_map
        intersectedMap = mapper.get_quasi_intersected_mappings(intersectedMap, candidate_map)

    # return mapper.remove_solved_letters_from_mapping(intersectedMap) #TODO jakis blad
    return intersectedMap


if __name__ == '__main__':
    mapper = SimpleSubstitutionMapper()
    #
    # mapping_empty = mapper.get_blank()
    #
    # cipher_word = "HGHF"
    # candidate_1 = "THAT"
    #
    # map_from_word1 = mapper.make_mapping(cipher_word, candidate_1)
    #
    # candidate_2 = "HIGH"
    # map_from_word2 = mapper.make_mapping(cipher_word, candidate_2)
    #
    # final_map = mapper.get_quasi_intersected_mappings(map_from_word1, map_from_word2)
    #
    # print(map_from_word2)
    # print(final_map)


    #24.11.2025
    map_ = mapper.create_final_mapping(["HGHF"], WordPattern())
    # map_['A'] = set('B')
    print(map_)

    mapper.remove_solved_letters_from_mapping(map_)

    print(map_)

    msg = "Perpendicular reconstruction"
    cipher = SubstitutionCipher()
    key = cipher.get_random_key()
    enc = cipher.encrypt(msg, key)

    print(f"Encrypting message: '{msg}' with key: '{key}'")
    print(f"Encrypted message: '{enc}'")
    print(crack(enc))