class EnglishDetector:
    UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SYMBOLS = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

    def __init__(self, dict_path="../dictionary.txt"):
        self.eng_words = self._load_dict(dict_path)

    def _load_dict(self, path):
        with open(path) as file:
            content = file.read()
            content_list = content.split('\n')
            return set(content_list)

    def remove_non_letters(self, message):
        letters_only = [symbol for symbol in message if symbol in self.SYMBOLS]
        return ''.join(letters_only)

    def get_eng_percentage(self, message):
        potential_word_list = self.remove_non_letters(message).split()
        if not potential_word_list:
            return 0.0
        matches = sum(1 for word in potential_word_list if word.upper() in self.eng_words)
        return matches / len(potential_word_list)

    def is_eng(self, message, words_percentage=50, letters_percentage=60):
        words_match = self.get_eng_percentage(message) * 100 >= words_percentage
        letters_match = (len(self.remove_non_letters(message)) / len(message)) * 100 >= letters_percentage
        return words_match and letters_match


if __name__ == "__main__":
    detector = EnglishDetector()
    message = "Once a set is created, you cannot change its items, but you can add new items. To add one item to a set use the add() method."
    print(message, "=", detector.is_eng(message))