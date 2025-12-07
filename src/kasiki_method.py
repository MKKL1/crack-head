import re

def spacing_between_sequences(message: str) -> dict[str, list[int]]:
    clean_msg = re.sub(r'[^A-Z]', '', message.upper())
    msg_len = len(clean_msg)

    sequences: dict[str, list[int]] = {}

    for seq_len in range(3, 5):
        for j in range(msg_len-seq_len+1):
            seq = clean_msg[j:j+seq_len]
            if sequences.get(seq) is None:
                sequences[seq] = []
            sequences[seq].append(j)

    sequences_spacing: dict[str, list[int]] = {}
    for seq, indices in sequences.items():
        if len(indices) < 2:
            continue

        spacing = []
        first = indices[0]
        for i in range(1, len(indices)):
            second = indices[i]
            spacing.append(abs(first - second))

        sequences_spacing[seq] = spacing

    return sequences_spacing

if __name__ == '__main__':
    test = """jwetx osdafhuir dfgiorhk sdaith ldfuhioiosh se txoiht gdfse sda"""

    spacing_between_sequences(test)