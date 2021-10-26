def trim_sequences(seq_1, seq_2):
    """
    If called after checking sequences for equality, should work correctly.
    """
    start_index = 0
    end_index = 0

    for base_1, base_2 in zip(seq_1, seq_2):
        if base_1 == base_2:
            start_index += 1
        else:
            break
    seq_1 = seq_1[start_index:]
    seq_2 = seq_2[start_index:]

    for base_1, base_2 in zip(reversed(seq_1), reversed(seq_2)):
        if base_1 == base_2:
            end_index += 1
        else:
            break

    if end_index != 0:
        seq_1 = seq_1[:-end_index]
        seq_2 = seq_2[:-end_index]
    return seq_1, seq_2, start_index, end_index


def build_matrix(seq_1, seq_2, config):
    if seq_1 == seq_2:
        return None
