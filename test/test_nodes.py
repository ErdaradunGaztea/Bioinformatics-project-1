from src.matrix import Node, Direction

default_config = {
    "same_award": 2,
    "gap_penalty": 1,
    "difference_penalty": 2,
    "max_seq_length": 10000,
    "max_number_paths": 100
}
n1 = Node(None, None, None, default_config)
n2 = Node(None, None, None, default_config)
n3 = Node(None, None, None, default_config)


def test_compute_node_value():
    n1.value = 7
    n2.value = 4
    n3.value = 3
    n4 = Node(n1, n2, n3, default_config)
    n4.compute_value("K", "K")
    assert n4.value == 6
    assert len(n4.directions) == 2
    assert Direction.LEFT in n4.directions
    assert Direction.DIAGONAL in n4.directions
