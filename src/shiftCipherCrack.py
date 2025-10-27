import shiftCipher as sC
import pyperclip

def crackShiftCipher(cipher):
    for keyValue in range(2, len(cipher)-1):
        plainText = sC.shiftDecrypt(cipher, keyValue)
        print('Potencjalna treść wiadomosći dla klucza o wartości {0} to: {1}'.format(keyValue, plainText))
