
def find_repeated_dna(sequence: str):  # LeetCode Q.187.
    visited_dna, repeated_dna = set(), set()
    for start_idx in range(len(sequence) - 9):
        dna = sequence[start_idx: start_idx + 10]
        if dna not in visited_dna:
            visited_dna.add(dna)
            continue
        repeated_dna.add(dna)

    return list(repeated_dna)
