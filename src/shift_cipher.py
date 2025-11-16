import math

from src.detect_english import EnglishDetector


def shift_encrypt(message: str, key: int):
    res_list = [''] * key
    for i in range(len(message)):
        j = i % key
        res_list[j] += message[i]
    cipher = ''.join(res_list)
    return cipher


def shift_decrypt(cipher: str, key: int):
    cipher_length = len(cipher)
    columns_number = math.ceil(cipher_length / key)
    rows_number = key
    empty_cells_number = rows_number * columns_number - cipher_length
    res_list = [''] * columns_number

    h = 0
    for i in range(cipher_length):
        current_row_no = (i + h) // columns_number
        current_col_no = (i + h) % columns_number

        if (current_row_no >= rows_number - empty_cells_number) and (current_col_no == columns_number - 1):
            h += 1
            res_list[0] += cipher[i]
        else:
            res_list[current_col_no] += cipher[i]
    plain_text = ''.join(res_list)
    return plain_text

def crack_shift_cipher(cipher):
    for keyValue in range(2, len(cipher)-1):
        plain_text = shift_decrypt(cipher, keyValue)
        print('key={0}     msg={1}'.format(keyValue, plain_text))

def crack_shift_cipher_smart(cipher, eng_detector: EnglishDetector):
    candidates = []

    max_key = len(cipher) // 2
    for key_value in range(2, max_key + 1):
        plain_text = shift_decrypt(cipher, key_value)

        if eng_detector.is_eng(plain_text):
            candidates.append({"key": key_value, "text": plain_text})

    return candidates

if __name__ == '__main__':
    # message_ = input('Wprowadź treść wiadomości: ')
    # key_ = input('Wprowadź klucz: ')
    # mode_ = input('Wprowadź tryb: 0 = dekrypcja lub 1 = enkrypcja: ')
    # messageLength = len(message_)
    # outcome = ''
    #
    # if mode_ == '1':
    #     outcome = shift_encrypt(message_, int(key_))
    # else:
    #     outcome = shift_decrypt(message_, int(key_))
    # pyperclip.copy(outcome)

    shift_encrypt("siemaelo", 4)

    franken = """You will rejoice to hear that no disaster has accompanied the
    commencement of an enterprise which you have regarded with such evil
    forebodings.  I arrived here yesterday, and my first task is to assure
    my dear sister of my welfare and increasing confidence in the success
    of my undertaking."""

    secret_key = 23
    encrypted = shift_encrypt(franken, secret_key)
    crack_shift_cipher_smart(encrypted, EnglishDetector("../dictionary.txt"))

