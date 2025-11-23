import sys

from src.defs import AlgorithmMode

class SubstitutionCipher:
    def __init__(self, symbols: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self.symbols = symbols
        self.length = len(symbols)

    def get_random_key(self) -> str:
        import random
        symbols_list = list(self.symbols)
        random.shuffle(symbols_list)
        return ''.join(symbols_list)

    def key_is_valid(self, key: str) -> bool:
        if len(key) != self.length:
            return False

        key_sorted = sorted(list(key))
        symbols_sorted = sorted(list(self.symbols))

        return key_sorted == symbols_sorted

    def encrypt(self, message: str, key: str) -> str:
        if not self.key_is_valid(key):
            raise ValueError(
                f"Invalid key. Key must be a permutation of the alphabet: {self.symbols}"
            )
        return self._translate_message(message, key, AlgorithmMode.Encryption)

    def decrypt(self, cipher: str, key: str) -> str:
        if not self.key_is_valid(key):
            raise ValueError(
                f"Invalid key. Key must be a permutation of the alphabet: {self.symbols}"
            )
        return self._translate_message(cipher, key, AlgorithmMode.Decryption)

    def _translate_message(self, text: str, key: str, mode: AlgorithmMode) -> str:
        translated = ''

        s1 = self.symbols
        s2 = key

        if mode == AlgorithmMode.Decryption:
            s1, s2 = s2, s1

        for symbol in text:
            if symbol.upper() in s1:
                index = s1.find(symbol.upper())

                if symbol.isupper():
                    translated += s2[index].upper()
                else:
                    translated += s2[index].lower()
            else:
                translated += symbol

        return translated

    def interactive_mode(self):
        message_ = input('Wprowadź wiadomość: ')
        print('Naciśnij (L) jeśli chcesz by klucz był losowany przez system, w przeciwnym razie Enter: ')
        response_ = input('> ')

        if response_.strip().upper().startswith('L'):
            key_ = self.get_random_key()
            print('Wylosowano klucz (permutację alfabetu): ' + key_)
        else:
            key_ = input('Wpisz własny klucz: ')

            if not self.key_is_valid(key_):
                sys.exit('Zaproponowany klucz nie jest permutacją alfabetu. ')

        mode_ = input('Wybierz tryb pracy: 1-enkrypcja lub 0-dekrypcja: ')
        mode = int(mode_)

        if mode == 1:
            outcome = self.encrypt(message_, key_)
            print('Wiadomość po enkrypcji: ')
        elif mode == 0:
            outcome = self.decrypt(message_, key_)
            print('Wiadomość po dekrypcji: ')
        else:
            sys.exit('Nieprawidłowy tryb. Wybierz 0 lub 1.')

        print(outcome)


if __name__ == '__main__':
    cipher = SubstitutionCipher()

    c1 = "Kjcbzlv G ijtup śiglsjirt ijtvqj ugregrbqgr vsjvjilłj jkylbjilup kyzrz khłqjiugql Oygszl Urmral vzpoy LCOWDX. Vzpoyjilugr jcmpilłj vgę zl kjejbp vzlbnjiugbp Kjagmghvzl. Vlel slmagbl ipkrługlul mpłl trculq agsryleg i vkjvóm ajvjip, męcąb zulul ipłąbzugr ulclibp g jcmgjykp"
    msg1 = cipher.decrypt(c1, "LMBCROWNGTQAEUJKFYVSHDIXPZ")
    print("Przykład 1:")
    print(msg1)
    print()

    c2 = "Vidbuhmtqbd Ghcqwqrvid oh fhyids vijlfr zhthdcldweojbitekh mjzjśchtj m vodfhżjothśbq gfiei kfebnqekh uqvohfjnd Ghcqwqrvid. Vijlf oet gfijgqvrse ndżyes cqoefie cqbiwę, meyłrk vgebsdctes odwecq 0 25 nhzófndbu"
    msg2 = cipher.decrypt(c2, "DWBYELKUQSNCZTHGXFVORAMPJI")
    print("Przykład 2:")
    print(msg2)
    print()

    print("================")
    cipher.interactive_mode()