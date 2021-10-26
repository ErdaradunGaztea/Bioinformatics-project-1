from src import build_matrix, trim_sequences

default_config = {
    "same_award": 2,
    "gap_penalty": 1,
    "difference_penalty": 2,
    "max_seq_length": 10000,
    "max_number_paths": 100
}
seq_1 = "KYNPMCILNYRNECETCDIYLRTINLWWGKDEMEKH"
seq_2 = "MEINDMHDIWRLQLFHWCTHTFIFFWRRINNCLLTL"
seq_3 = "KYNPMCILNWRLQLFHWCTHTFIFFWRWGKDEMEKH"


def test_all_equal():
    """
    If both sequences are the same, do not create the matrix.
    """
    matrix = build_matrix(seq_1, seq_1, default_config)
    assert matrix is None


def test_trimmed_sequences():
    """
    Identical pre- and suffixes are removed.
    """
    seq_1_trimmed, seq_3_trimmed = trim_sequences(seq_1, seq_3)
    assert seq_1_trimmed == "YRNECETCDIYLRTINLW"
    assert seq_3_trimmed == "WRLQLFHWCTHTFIFFWR"


def test_no_trim_sequences():
    """
    Sequences can remain not trimmed when first and last bases are different.
    """
    seq_1_trimmed, seq_2_trimmed = trim_sequences(seq_1, seq_2)
    assert seq_1_trimmed == seq_1
    assert seq_2_trimmed == seq_2
