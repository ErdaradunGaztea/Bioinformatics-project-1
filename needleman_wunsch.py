import sys
from argparse import ArgumentParser

from src.config import parse_config
from src.extend_paths import extend_paths
from src.matrix import trim_sequences, build_matrix
from src.path import follow_path, Path
from src.read_sequence import read_sequence
from src.write_paths import write_paths

parser = ArgumentParser()
parser.add_argument("-a", "--seq1", help="path to 1st sequence in FASTA format")
parser.add_argument("-b", "--seq2", help="path to 2nd sequence in FASTA format")
parser.add_argument("-c", "--config", help="path to YAML config file", default="default_config.yml")
parser.add_argument("-o", "--output", help="path to output file")

if __name__ == "__main__":
    args = parser.parse_args()
    seq_1 = read_sequence(args.seq1)
    seq_2 = read_sequence(args.seq2)
    config = parse_config(args.config)

    sys.setrecursionlimit(config['max_seq_length'] * 2)

    # Default values when sequences are identical.
    paths = [Path(seq_1, seq_2)]
    score = config['same_award'] * len(seq_1)
    # But more often than not, they won't be...
    if seq_1 != seq_2:
        seq_1_trim, seq_2_trim, start_index, end_index = trim_sequences(seq_1, seq_2)
        matrix = build_matrix(seq_1_trim, seq_2_trim, config)
        paths, score = follow_path(matrix, seq_1_trim, seq_2_trim, config)
        paths = extend_paths(paths, seq_1, seq_2, start_index, end_index)

    write_paths(args.output, paths, score)
