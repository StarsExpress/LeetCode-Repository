
def reduce_half_integers(integers: list[int]):  # LeetCode Q.1338.
    if len(integers) <= 0:
        raise IndexError('Empty integers.')

    distinct_ints = set(integers)
    if len(distinct_ints) == 1:
        return 1

    counts = dict(zip(distinct_ints, [0] * len(distinct_ints)))  # Dict of each int's count.
    for integer in integers:
        counts[integer] += 1

    counts = list(counts.values())  # List of counts.
    counts.sort(reverse=True)

    target_size, cumulated_size, current_idx = len(integers) // 2, counts[0], 1
    if len(integers) % 2 == 1:
        target_size += 1

    while True:
        if cumulated_size >= target_size:
            return current_idx

        cumulated_size += counts[current_idx]
        current_idx += 1
