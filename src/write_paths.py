def write_paths(filename, paths, score):
    with open(filename, "w") as f:
        f.write("SCORE = {0}\n".format(score))
        for path in paths:
            f.write("\n")
            f.write(path.seq_1 + "\n")
            f.write(path.seq_2 + "\n")
