from src.affine_cipher import AffineCipher
from src.crypto_math import gcd
from src.detect_english import EnglishDetector

def crack_affine_cipher(cipher):
    ed = EnglishDetector("../dictionary.txt")
    SYMBOLS_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,.'"
    affine = AffineCipher(SYMBOLS_EN)

    length = len(SYMBOLS_EN)
    for key in range(length**2):
        keyA = affine.get_key_parts(key)[0]
        if gcd(keyA, length) != 1:
            continue

        plainText = affine.decrypt(cipher, key)
        if ed.is_eng(plainText):
            print(f"Potencjalny tekst jawny '{plainText}'")
            print("Wpisz 'yes' zeby potwierdzic")
            response = input('> ')
            if response.lower() == "yes":
                return key, plainText

    return None, None

if __name__ == '__main__':
    cipher = "V?vIb'6?vthvkbdkIbvw'KbvU4bUv4WvQ'P'4N'v'6v'vyb6DI?vdivCDyy4N'WbvlbI466'AvJWidyP'?4dWvl4W46?byvq'W'vldyy46vq4YdWvw'6v6'4UAv'6v6b'yNwv'WUvyb6NDbvbiidy?6vNdW?4WDbv'WUv'D?wdy4?4b6v?yfv?dvpb?v'4Uv?dvw'yU-w4?v'yb'6HSwbvwDyy4N'WbAvdWbvdiv?wbvPd6?vkdRbyiDIv?dv6?y4Bbv?wbvj'y4GGb'WAvw'6v'I6dvB4IIbUv'?vIb'6?v8ovkbdkIbv4WvC'4?4Avdii4N4'I6v6'4UH"
    found_key, msg = crack_affine_cipher(cipher)

    print("found key:", found_key)
    print("msg:", msg)