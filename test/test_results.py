import numpy as np

from src.matrix import build_matrix
from src.path import follow_path

default_config = {
    "same_award": 2,
    "gap_penalty": 1,
    "difference_penalty": 2,
    "max_seq_length": 10000,
    "max_number_paths": 100
}
modified_config = {
    "same_award": 3,
    "gap_penalty": 2,
    "difference_penalty": 3,
    "max_seq_length": 10000,
    "max_number_paths": 100
}
seq_1 = "KY"
seq_2 = "MEI"
seq_3 = "PAAD"
seq_4 = "MAAR"

extract_value = np.vectorize(lambda x: x.value)


def test_matrix():
    matrix = build_matrix(seq_1, seq_2, default_config)
    assert matrix.shape == (3, 4)
    assert np.equal(
        extract_value(matrix),
        np.array([[0, -1, -2, -3], [-1, -2, -3, -4], [-2, -3, -4, -5]])
    ).all()


def test_score():
    matrix = build_matrix(seq_1, seq_2, default_config)
    _, score = follow_path(matrix, seq_1, seq_2, default_config)
    assert score == -5


def test_one_path():
    matrix = build_matrix(seq_3, seq_4, modified_config)
    paths, score = follow_path(matrix, seq_3, seq_4, modified_config)
    assert len(paths) == 1
    assert paths[0].seq_1 == "PAAD"
    assert paths[0].seq_2 == "MAAR"
    assert score == 0


def test_multiple_paths():
    matrix = build_matrix(seq_3, seq_4, default_config)
    paths, score = follow_path(matrix, seq_3, seq_4, default_config)
    assert len(paths) == 9
    assert score == 0
    assert "P-AA-D" in [path.seq_1 for path in paths]
