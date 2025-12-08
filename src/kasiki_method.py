import re


def spacing_between_sequences(message: str) -> dict[str, list[int]]:
    """
    Find spacing between unknown, repeating sequences (3-5 length)
    """
    clean_msg = re.sub(r'[^A-Z]', '', message.upper())
    msg_len = len(clean_msg)

    sequences: dict[str, list[int]] = {}

    for seq_len in range(3, 5):
        for j in range(msg_len - seq_len + 1):
            seq = clean_msg[j:j + seq_len]

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


def get_factors(number: int, max_key_length: int = 16) -> list[int]:
    """
    Get factors of a number. eg. 16 => 16,8,4,2
    """
    factors = []

    for i in range(2, max_key_length + 1):
        if number % i == 0:
            factors.append(i)

    return factors


def get_most_common_factors(sequences_spacings: dict[str, list[int]]) -> list[tuple[int, int]]:
    """
    Sort by most often appearing factor. eg, {'ETX': [38]... => [(2,5), (4,1), (x, count)]
    """
    factors_count = {}

    for seq_list in sequences_spacings.values():
        for distance in seq_list:
            current_factors = get_factors(distance)
            for factor in current_factors:
                factors_count[factor] = factors_count.get(factor, 0) + 1

    return sorted(factors_count.items(), key=lambda x: x[1], reverse=True)


def get_kasiski_examination_result(ciphertext: str) -> list[int]:
    """
    Extract factors [(2,5), (4,1), (x, count)] => [2,4,x,...]
    """
    spacings = spacing_between_sequences(ciphertext)
    common_factors = get_most_common_factors(spacings)
    allLikelyKeyLengths = [item[0] for item in common_factors]

    return allLikelyKeyLengths


if __name__ == '__main__':
    test_cipher = "jwetx osdafhuir dfgiorhk sdaith ldfuhioiosh se txoiht gdfse sda"

    spacings = spacing_between_sequences(test_cipher)
    print(f"spacing: {spacings}")

    common = get_most_common_factors(spacings)
    print(f"most common factors (factor, count): {common}")

    likely_keys = get_kasiski_examination_result(test_cipher)
    print(f"Likely Key Lengths: {likely_keys}")
