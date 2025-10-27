UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def load_dict():
    with open("../../dictionary.txt") as file:
        content = file.read()
        contentList = content.split('\n')

        englishWords = {word: None for word in contentList}
    return englishWords

ENG_WORDS = load_dict()

def remove_non_letters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in SYMBOLS:
            lettersOnly.append(symbol)

    return ''.join(lettersOnly)

def get_eng_count(message):
    potentialWordList = remove_non_letters(message).split()

    if potentialWordList == []:
        return 0.0
    matches = 0
    for word in potentialWordList:
        if word.upper() in ENG_WORDS:
            matches += 1

    return matches/len(potentialWordList)

def is_eng(message, words_percentage = 50, letters_percentage = 60):
    wordsMatch = get_eng_count(message)*100 >= words_percentage
    lettersMatch = (len(remove_non_letters(message))/len(message))*100 >= letters_percentage
    outcome = wordsMatch and lettersMatch

    return outcome

def check_and_print(message):
    print(message, "=" ,is_eng(message))

if __name__ == "__main__":
    check_and_print("Once a set is created, you cannot change its items, but you can add new items. To add one item to a set use the add() method.")