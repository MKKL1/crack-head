
from caesar_crack import decrypt_caesar, encrypt_caesar

if __name__ == "__main__":
    mode = input("Decryption (0)/Encryption (1): ")
    message = input("Message: ")
    key = input("Key: ")

    if mode == "0":
        res = decrypt_caesar(message, int(key))
    elif mode == "1":
        res = encrypt_caesar(message, int(key))
    else:
        exit("nie")

    print(res)