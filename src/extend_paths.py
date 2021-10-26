def extend_paths(paths, seq_1, seq_2, start_index, end_index):
    prefix_1 = seq_1[:start_index]
    prefix_2 = seq_2[:start_index]
    suffix_1 = "" if end_index == 0 else seq_1[-end_index:]
    suffix_2 = "" if end_index == 0 else seq_2[-end_index:]

    for path in paths:
        path.seq_1 = prefix_1 + path.seq_1 + suffix_1
        path.seq_2 = prefix_2 + path.seq_2 + suffix_2
    return paths
