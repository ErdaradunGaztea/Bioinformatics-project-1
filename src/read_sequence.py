from Bio.SeqIO import read


def read_sequence(filename):
    return read(filename, "fasta").seq
