from src.caesar_cipher import crack_caesar, decrypt_caesar, encrypt_caesar

if __name__ == "__main__":
    # crack_caesar("""0iEŃJWiŚXÓKĘKiTNJĘSĆJiwWŁJWŚŹińĘŹĄSiRSĄXJĘiRÓLSŹZaÓXĄMiRŁĄŃZiŚRJŚLÓXĆPXliwĘHÓiaÓŃĄiCĄSEŹÓiŻŁĘiŚJFiĆŹWMĄiJiNJĄMĄiCĄSEŹÓiLSXĄXĘiŚŃZli4ÓRSÓŚJMĄiHÓiÓiRÓŹÓŚUĄŃJĘiXiEÓNW,iĄŁĘiÓŚUĄUĘĆŹŃJĘiwWŁJWŚŹiŹEĘĆZEÓXĄMiŚJFiRÓKĄXJDiŃĄiÓCSĄEĄĆIiŚĘŃĄUWliżĄXĘUiXiESÓEŹĘiŃĄiÓCSĄEZiÓUSŹZNĄMiŁJŚUiŹiÓŚUSŹĘaĘŃJĘN,iĄŁĘiŚRJĘŚŹZMiŚJFiJiŚĆIÓXĄMiHÓiŃĄiRPŻŃJĘKl""")
    crack_caesar("""P2ćhYn29ZpŚkŚ2ćhkpólmŚfh2fŚńZm2ń2śżśx2khćn526kębŚ2BęjZkbnę2KhlóclćbZah2jhlenabńŚeŚ2lbŹ2fbę2cŚćh2pŚębZffbćbZę2YdŚ2cZc2UŚkYpbZc2lćhęjdbćhńŚfóWą2lpóŻkiń,2ćmikZ2Uóeó2pUóm2mknYfZ2Yh2hjŚfhńŚfbŚ2YdŚ2khlóclćbZah2ńhclćŚ,2YpbŹćb2WpZęn2fbZębZWWó2b2ŚnlmkbŚWWó2ćkójmhŚfŚdbmóWó2fbZ2ębZdb2ńbŹćlpóWą2jkhUdZęiń2p2hYWpómŚfbZę2móWą2ńbŚYhęhłWb5""")
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