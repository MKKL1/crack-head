def get_word_pattern(word:str) -> list[int]:
    letters = {}
    result = [0] * len(word)

    k = 0
    for i, e in enumerate(word):
        if e in letters:
            result[i] = letters[e]
        else:
            result[i] = k
            letters[e] = k
            k += 1

    return result

def load_dict(path):
    with open(path) as file:
        patterns = {}
        content = file.read()
        content_list = content.split('\n')

        for word in content_list:
            patterns[word] = get_word_pattern(word)
        return patterns

def get_words_from_pattern(word:str, patterns:dict[str, list[int]]) -> list[str]:
    #TODO 3,4
    pass

if __name__ == '__main__':
    print(get_word_pattern("banan"))

    d = load_dict("../dictionary.txt")

    print(d)