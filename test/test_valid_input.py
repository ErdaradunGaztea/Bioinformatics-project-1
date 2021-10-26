import numpy as np

from src.matrix import build_matrix

default_config = {
    "same_award": 2,
    "gap_penalty": 1,
    "difference_penalty": 2,
    "max_seq_length": 10000,
    "max_number_paths": 100
}
seq_1 = "KY"
seq_2 = "MEI"

extract_value = np.vectorize(lambda x: x.value)


def test_matrix():
    matrix = build_matrix(seq_1, seq_2, default_config)
    assert matrix.shape == (3, 4)
    assert np.equal(
        extract_value(matrix),
        np.array([[0, -1, -2, -3], [-1, -2, -3, -4], [-2, -3, -4, -5]])
    ).all()
