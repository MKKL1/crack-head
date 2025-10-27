import pyperclip, math


def main():
    message_ = input('Wprowadź treść wiadomości: ')
    key_ = input('Wprowadź klucz: ')
    mode_ = input('Wprowadź tryb: 0 = dekrypcja lub 1 = enkrypcja: ')
    messageLength = len(message_)
    outcome = ''

    if mode_ == '1':
        outcome = shiftEncrypt(message_, int(key_))
    else:
        outcome = shiftDecrypt(message_, int(key_))
    pyperclip.copy(outcome)


def shiftEncrypt(message, key):
    resList = [''] * key
    for i in range(len(message)):
        j = i % key
        resList[j] += message[i]
    cipher = ''.join(resList)
    # print('Oto zaszyfrowana treść: ', cipher)
    return cipher


def shiftDecrypt(cipher, key):
    cipherLength = len(cipher)
    columnsNumber = math.ceil(cipherLength / key)
    rowsNumber = key
    emptyCellsNumber = rowsNumber * columnsNumber - cipherLength
    resList = [''] * columnsNumber

    h = 0
    for i in range(cipherLength):
        currentRowNo = (i + h) // columnsNumber
        currentColNo = (i + h) % columnsNumber

        if (currentRowNo >= rowsNumber - emptyCellsNumber) and (currentColNo == columnsNumber - 1):
            h += 1
            resList[0] += cipher[i]
        else:
            resList[currentColNo] += cipher[i]
    plainText = ''.join(resList)
    return plainText


if __name__ == '__main__':
    main()

