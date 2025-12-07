class FrequencyAnalyzer:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

    def get_letter_count(self, message: str) -> dict[str, int]:
        letter_map = {char: 0 for char in self.SYMBOLS}

        for char in message.upper():
            if char in letter_map:
                letter_map[char] += 1

        return letter_map

    def get_frequency_order(self, message: str) -> str:
        counts = self.get_letter_count(message)
        sorted_chars = sorted(self.SYMBOLS, key=lambda char: (-counts[char], self.ETAOIN.find(char)))
        return "".join(sorted_chars)

    def get_english_frequency_match_score(self, message: str) -> int:
        freq_order = self.get_frequency_order(message)

        frequent_eng = self.ETAOIN[:6]
        rare_eng = self.ETAOIN[-6:]

        most_freq_msg = freq_order[:6]
        least_freq_msg = freq_order[-6:]

        score = 0

        # Check top 6 matches
        for char in most_freq_msg:
            if char in frequent_eng:
                score += 1

        # Check bottom 6 matches
        for char in least_freq_msg:
            if char in rare_eng:
                score += 1

        return score


if __name__ == "__main__":
    analyzer = FrequencyAnalyzer()

    test = """I am already far north of London, and as I walk in the streets of
Petersburgh, I feel a cold northern breeze play upon my cheeks, which
braces my nerves and fills me with delight.  Do you understand this
feeling?  This breeze, which has travelled from the regions towards
which I am advancing, gives me a foretaste of those icy climes.
Inspirited by this wind of promise, my daydreams become more fervent"""
    score = analyzer.get_english_frequency_match_score(test)
    print(f"Score:  {score}")