import pprint

class WordPattern:
    def __init__(self, dict_path="../dictionary.txt"):
        self.dict_path = dict_path
        self.patterns_map: dict[tuple[int, ...], list[str]] = self._load_patterns()

    @staticmethod
    def get_word_pattern(word: str) -> tuple[int, ...]:
        word = word.upper()
        letters = {}
        result = []
        next_num = 0

        for letter in word:
            if letter not in letters:
                letters[letter] = next_num
                next_num += 1
            result.append(letters[letter])

        return tuple(result)

    def _load_patterns(self) -> dict[tuple[int, ...], list[str]]:
        patterns_map = {}

        with open(self.dict_path) as file:
            content = file.read()
            word_list = content.split('\n')

            for word in word_list:
                word = word.strip()
                if not word:
                    continue
                pattern = self.get_word_pattern(word)

                if pattern not in patterns_map:
                    patterns_map[pattern] = []

                patterns_map[pattern].append(word)

        return patterns_map

    def get_words_from_pattern(self, cipher_word: str) -> list[str]:
        target_pattern = self.get_word_pattern(cipher_word)

        if target_pattern in self.patterns_map:
            return self.patterns_map[target_pattern]
        else:
            return []


if __name__ == '__main__':
    helper = WordPattern("../dictionary.txt")

    test_word = "BANAN"
    print(f"Pattern for {test_word}: {helper.get_word_pattern(test_word)}")

    matches = helper.get_words_from_pattern(test_word)

    print(f"Words matching pattern of '{test_word}':")
    pprint.pprint(matches[:10])