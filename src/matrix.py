import numpy as np
from enum import Enum


class Direction(Enum):
    LEFT = "left"
    DIAGONAL = "diag"
    TOP = "top"


class Node:
    def __init__(self, left, diag, top, config):
        self.value = 0
        self.left = left
        self.diag = diag
        self.top = top
        self.config = config
        self.directions = []

    def compute_value(self, base_1, base_2):
        left_value = self.left.value - self.config['gap_penalty']
        top_value = self.top.value - self.config['gap_penalty']
        if base_1 == base_2:
            diag_value = self.diag.value + self.config['same_award']
        else:
            diag_value = self.diag.value - self.config['difference_penalty']

        self.value = max(left_value, top_value, diag_value)
        if left_value == self.value:
            self.directions.append(Direction.LEFT)
        if diag_value == self.value:
            self.directions.append(Direction.DIAGONAL)
        if top_value == self.value:
            self.directions.append(Direction.TOP)

        return self


class CornerNode:
    def __init__(self):
        self.value = 0
        self.directions = []


class EdgeNode:
    def __init__(self, parent, direction, config):
        self.value = parent.value - config['gap_penalty']
        self.left = parent if direction == Direction.LEFT else None
        self.top = parent if direction == Direction.TOP else None
        self.directions = [direction]


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

    seq_1_trim, seq_2_trim, start_index, end_index = trim_sequences(seq_1, seq_2)

    nodes = np.empty((len(seq_1_trim) + 1, len(seq_2_trim) + 1), dtype=Node)
    nodes[0, 0] = CornerNode()
    for index in range(len(seq_1_trim)):
        nodes[1 + index, 0] = EdgeNode(nodes[index, 0], Direction.TOP, config)
    for index in range(len(seq_2_trim)):
        nodes[0, 1 + index] = EdgeNode(nodes[0, index], Direction.LEFT, config)

    # build actual matrix
    # could be optimized, as we know from trimming that the first and the last elements of both seq's are different
    for row in range(len(seq_1_trim)):
        for column in range(len(seq_2_trim)):
            nodes[row + 1, column + 1] = Node(
                nodes[row + 1, column], nodes[row, column], nodes[row, column + 1], config
            ).compute_value(seq_1_trim[row], seq_2_trim[column])

    return nodes
