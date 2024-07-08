
def find_1st_missing_positive(integers: list[int]):  # LeetCode Q.41.
    unique_ints = set(integers)
    unique_positives = set(range(1, len(unique_ints) + 1))
    unique_positives -= unique_positives & unique_ints  # "Remaining" positives.
    if len(unique_positives) <= 0:  # Input integers are from 1 to len(integers).
        return len(unique_ints) + 1
    return min(unique_positives)
