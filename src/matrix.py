class Node:
    def __init__(self, left, diag, top, config):
        self.value = 0
        self.left = left
        self.diag = diag
        self.top = top
        self.config = config
        self.paths = []

    def compute_value(self, base_1, base_2):
        left_value = self.left.value - self.config['gap_penalty']
        top_value = self.top.value - self.config['gap_penalty']
        if base_1 == base_2:
            diag_value = self.diag.value + self.config['same_award']
        else:
            diag_value = self.diag.value - self.config['difference_penalty']

        self.value = max(left_value, top_value, diag_value)
        if left_value == self.value:
            self.paths.append(self.left)
        if diag_value == self.value:
            self.paths.append(self.diag)
        if top_value == self.value:
            self.paths.append(self.top)


class CornerNode:
    def __init__(self):
        self.value = 0
        self.paths = []


class EdgeNode:
    def __init__(self, parent, config):
        self.value = parent.value - config['gap_penalty']
        self.paths = [parent]


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
