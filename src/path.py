from copy import deepcopy

from src.matrix import Direction


def identity(x): return x


class Path:
    def __init__(self, seq_1="", seq_2=""):
        self.seq_1 = seq_1
        self.seq_2 = seq_2

    def append_bases(self, base_1, base_2):
        self.seq_1 = base_1 + self.seq_1
        self.seq_2 = base_2 + self.seq_2
        return self


class PathStore:
    def __init__(self, seq_1, seq_2, config):
        self.seq_1 = seq_1
        self.seq_2 = seq_2
        self.config = config

    def compute(self, path, node, index_1, index_2):
        if len(node.directions) == 0:
            # We arrived at the corner edge, success!
            return [path]

        # To avoid copying when not necessary.
        copying_func = deepcopy
        if len(node.directions) == 1:
            copying_func = identity

        paths = []
        for direction in node.directions:
            # I was thinking about making this code prettier, but it wasn't worth the effort.
            if direction == Direction.LEFT:
                paths += self.compute(
                    copying_func(path).append_bases(self.seq_1[index_1], "-"),
                    node.left, index_1 - 1, index_2
                )
                if len(paths) >= self.config['max_number_paths']:
                    return paths
            if direction == Direction.DIAGONAL:
                paths += self.compute(
                    copying_func(path).append_bases(self.seq_1[index_1], self.seq_2[index_2]),
                    node.diag, index_1 - 1, index_2 - 1
                )
                if len(paths) >= self.config['max_number_paths']:
                    return paths
            if direction == Direction.TOP:
                paths += self.compute(
                    copying_func(path).append_bases("-", self.seq_2[index_2]),
                    node.top, index_1, index_2 - 1
                )
                if len(paths) >= self.config['max_number_paths']:
                    return paths
        return paths


def follow_path(nodes, seq_1, seq_2, config):
    score = nodes[-1, -1].value
    paths = PathStore(seq_1, seq_2, config).compute(Path(), nodes[-1, -1], len(seq_1) - 1, len(seq_2) - 1)
    return paths, score
