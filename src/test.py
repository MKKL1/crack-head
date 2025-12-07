SYMBOLS = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWXYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwxyzźż1234567890 !?."
encrypted = "SJhWT"
secret = "KEY"

# We assume that message contains only characters from SYMBOLS
message = ""
for i, encrypted_char in enumerate(encrypted):
    key_char = secret[i % len(secret)]

    encrypted_index = SYMBOLS.find(encrypted_char)
    key_index = SYMBOLS.find(key_char)

    #                      + CHANGED TO -
    new_index = (encrypted_index - key_index) % len(SYMBOLS)
    message += SYMBOLS[new_index]

print(message)  # HELLO