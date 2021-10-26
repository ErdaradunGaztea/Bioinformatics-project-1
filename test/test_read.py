from read_sequence import read_sequence


def test_read_fasta():
    seq = read_sequence('data/seq1.fasta')
    assert seq[4] == 'G'
