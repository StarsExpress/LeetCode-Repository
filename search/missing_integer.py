
def find_1st_missing_positive(integers: list[int]):
    unique_ints = set(integers)
    unique_positives = set(range(1, len(unique_ints) + 1))  # From 1 to unique ints count.
    unique_positives -= unique_positives & unique_ints  # The "remaining" positives.
    if len(unique_positives) <= 0:  # "Unique & consecutive positives" inputs wipe away everything.
        return len(unique_ints) + 1
    return min(unique_positives)
