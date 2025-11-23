import math

from src.detect_english import EnglishDetector


class ShiftCipher:
    """Transposition/Shift cipher with configurable symbol set."""

    def encrypt(self, message: str, key: int) -> str:
        """Encrypt message using shift cipher."""
        result_list = [''] * key
        for i, char in enumerate(message):
            column = i % key
            result_list[column] += char
        return ''.join(result_list)

    def decrypt(self, cipher: str, key: int) -> str:
        """Decrypt cipher using shift cipher."""
        cipher_length = len(cipher)
        columns_number = math.ceil(cipher_length / key)
        rows_number = key
        empty_cells_number = rows_number * columns_number - cipher_length
        result_list = [''] * columns_number

        h = 0
        for i in range(cipher_length):
            current_row_no = (i + h) // columns_number
            current_col_no = (i + h) % columns_number

            if (current_row_no >= rows_number - empty_cells_number and
                    current_col_no == columns_number - 1):
                h += 1
                result_list[0] += cipher[i]
            else:
                result_list[current_col_no] += cipher[i]

        return ''.join(result_list)

    def crack(self, cipher: str):
        """Brute force crack by trying all possible keys."""
        for keyValue in range(2, len(cipher) - 1):
            plain_text = self.decrypt(cipher, keyValue)
            print('key={0} msg={1}'.format(keyValue, plain_text))

    def crack_shift_cipher_smart(self, cipher, eng_detector: EnglishDetector):
        candidates = []

        max_key = len(cipher) // 2
        for key_value in range(2, max_key + 1):
            plain_text = self.decrypt(cipher, key_value)

            if eng_detector.is_eng(plain_text):
                candidates.append({"key": key_value, "text": plain_text})

        return candidates

# if __name__ == '__main__':
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

    # shift_encrypt("siemaelo", 4)
    #
    # franken = """You will rejoice to hear that no disaster has accompanied the
    # commencement of an enterprise which you have regarded with such evil
    # forebodings.  I arrived here yesterday, and my first task is to assure
    # my dear sister of my welfare and increasing confidence in the success
    # of my undertaking."""
    #
    # secret_key = 23
    # encrypted = shift_encrypt(franken, secret_key)
    # crack_shift_cipher_smart(encrypted, EnglishDetector("../dictionary.txt"))

if __name__ == '__main__':
    ceasar = ShiftCipher()
    key = 4
    msg = "siema elo"
    enc = ceasar.encrypt(msg, key)

    dec = ceasar.decrypt(enc, key)

    print("========Multiplicative cipher========")
    print(f"Encrypting message: '{msg}' with key: '{key}'")
    print(f"Encrypted message: '{enc}'")
    print(f"Decrypting: '{enc}' with key: '{key}'")
    print(f"Decrypted message: '{dec}'")