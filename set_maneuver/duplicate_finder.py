
def find_duplicate_integer(integers: list[int]):  # LeetCode Q.287.
    """Only 1 int repeats while others each occur once."""
    # (Sum of all ints - sum of unique ints) = repeated int * (occurrences - 1).
    unique_ints = set(integers)
    return (sum(integers) - sum(unique_ints)) // (len(integers) - len(unique_ints))


def seek_missed_integer(ints: list[int]):  # LeetCode Q.645.
    """
    Desired ints: 1 to n, but one is misplaced by another. Return [duplicate, missed int].
    """
    ints_1_to_n = set(range(1, len(ints) + 1))
    missed_int = (ints_1_to_n - set(ints)).pop()
    return [sum(ints) - sum(ints_1_to_n) + missed_int, missed_int]
