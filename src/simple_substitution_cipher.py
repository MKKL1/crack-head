import sys, random

from src.defs import AlgorithmMode

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mode = 0 #będziemy potrzebować globalnego zasięgu

def main():
    message_ = input('Wprowadź wiadomość: ')
    print('Naciśnij (L) jeśli chcesz by klucz był losowany przez system, w przeciwnymrazie Enter: ')
    response_ = input('> ')
    if response_.strip().upper().startswith('L'):
        key_ = get_random_key()
        print('Wylosowano klucz (permutację alfabetu): ' + key_)
    else:
        key_ = input('Wpisz własny klucz: ')

        if not key_is_valid(key_):
            sys.exit('Zaproponowany klucz nie jest permutacją alfabetu. ')

    mode_ = input('Wybierz tryb pracy: 1-enkrypcja lub 0-dekrypcja: ')
    mode = int(mode_)

    if mode == 1:
        outcome = substitution_encrypt(message_, key_)
        print('Wiadomość po enkrypcji: ')
    elif mode == 0:
        outcome = substitution_decrypt(message_, key_)
        print('Wiadomość po dekrypcji: ')
    print(outcome)

def get_random_key():
    symbolsList = list(SYMBOLS)
    random.shuffle(symbolsList)
    return ''.join(symbolsList)

def key_is_valid(key):
    keyListSorted = list(key).sort()
    symbolsList = list(SYMBOLS).sort()
    return keyListSorted == symbolsList

def substitution_encrypt(message, key):
    return translate_message(message, key, AlgorithmMode.Encryption)

def substitution_decrypt(message, key):
    return translate_message(message, key, AlgorithmMode.Decryption)

def translate_message(message, key, mode: AlgorithmMode):
    translated = ''
    s1 = SYMBOLS
    s2 = key

    if mode == AlgorithmMode.Decryption:
        s1, s2 = s2, s1

    for symbol in message:
        if symbol.upper() in s1:
            id = s1.find(symbol.upper())

            if symbol.isupper():
                translated += s2[id].upper()
            else:
                translated += s2[id].lower()
        else:
            translated += symbol

    return translated

if __name__ == '__main__':
    c1 = "Kjcbzlv G ijtup śiglsjirt ijtvqj ugregrbqgr vsjvjilłj jkylbjilup kyzrz khłqjiugql Oygszl Urmral vzpoy LCOWDX. Vzpoyjilugr jcmpilłj vgę zl kjejbp vzlbnjiugbp Kjagmghvzl. Vlel slmagbl ipkrługlul mpłl trculq agsryleg i vkjvóm ajvjip, męcąb zulul ipłąbzugr ulclibp g jcmgjybp"
    msg = substitution_decrypt(c1, "LMBCROWNGTQAEUJKFYVSHDIXPZ")
    print(msg)

    c2 = "Vidbuhmtqbd Ghcqwqrvid oh fhyids vijlfr zhthdcldweojbitekh mjzjśchtj m vodfhżjothśbq gfiei kfebnqekh uqvohfjnd Ghcqwqrvid. Vijlf oet gfijgqvrse ndżyes cqoefie cqbiwę, meyłrk vgebsdctes odwecq 0 25 nhzófndbu"
    msg2 = substitution_decrypt(c2, "DWBYELKUQSNCZTHGXFVORAMPJI")
    print(msg2)

    # main()