default_config = {
    "same_award": 2,
    "gap_penalty": 1,
    "difference_penalty": 2,
    "max_seq_length": 10000,
    "max_number_paths": 100
}
seq_1 = "KYNPMCILNYRNECETCDIYLRTINLWWGKDEMEKH"
seq_2 = "MEINDMHDIWRLQLFHWCTHTFIFFWRRINNCLLTL"


def test_all_equal():
    """
    If both sequences are the same, do not create the matrix.
    """
    matrix = build_matrix(seq_1, seq_1, default_config)
    assert matrix is None
