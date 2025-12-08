from operator import itemgetter
import itertools

from src.frequency_analysis import FrequencyAnalyzer
from src.vigenere.vigenere_cipher import VigenereCipher

testMsg='PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'


def get_concatenated_every_nth_letter(message, key_length, n):
    sub_sequence = [message[i] for i in range(n - 1, len(message), key_length)]
    return ''.join(sub_sequence)

#print(getConcatenatedEveryNthLetter(testMsg, 4, 1))
# PAEBABANZIAHAKDXAAAKIU


def attempt_crack_with_key_length(ciphertext, key_length):
    ciphertext_up = ciphertext.upper()
    all_frequency_scores = []
    frequency_analyzer = FrequencyAnalyzer()
    vigenere_cipher = VigenereCipher(symbols=frequency_analyzer.SYMBOLS)

    for n in range(1, key_length + 1):
        submessage_n = get_concatenated_every_nth_letter(ciphertext_up, key_length, n)
        frequency_scores_for_submessage_n = []

        for subKey in vigenere_cipher.symbols:
            decrypted_submessage_n = vigenere_cipher.decrypt(submessage_n,subKey*len(submessage_n))
            tuple_ = (subKey, frequency_analyzer.get_english_frequency_match_score(decrypted_submessage_n))
            frequency_scores_for_submessage_n.append(tuple_)

        frequency_scores_for_submessage_n.sort(key = itemgetter(1), reverse = True)

        all_frequency_scores.append(frequency_scores_for_submessage_n[:5])

    for i in range(len(all_frequency_scores)):
        scores = [tuple[1] for tuple in all_frequency_scores[i]]
        maxScoresOnly = [t for t in all_frequency_scores[i] if t[1] == max(scores)]
        all_frequency_scores[i] = maxScoresOnly

    potentialKeyLetters = []
    for list_ in all_frequency_scores:
        letterList = [t[0] for t in list_]
        potentialKeyLetters.append(letterList)

    possibleKeys = list(itertools.product(*potentialKeyLetters))
    print(possibleKeys)

    for p_key in possibleKeys:
        key = ''.join(p_key)
        dec = vigenere_cipher.decrypt(testMsg, key)
        print(f"key={key} msg={dec}")

if __name__ == "__main__":
    attempt_crack_with_key_length(testMsg, 4)