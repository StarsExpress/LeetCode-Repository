
def reduce_half_integers(integers: list[int]):  # LeetCode Q.1338.
    distinct_ints = set(integers)
    total_distinct_ints, total_ints = len(distinct_ints), len(integers)
    if total_distinct_ints == 1:
        return 1

    counts = dict(zip(distinct_ints, [0] * total_distinct_ints))  # Dict of each int's count.
    for integer in integers:
        counts[integer] += 1

    counts = list(counts.values())
    counts.sort(reverse=True)  # Start from bigger counts to minimize distinct ints used during reduction.

    target_size, cumulated_size, current_idx = total_ints // 2, counts[0], 1
    if total_ints % 2 == 1:
        target_size += 1

    while cumulated_size < target_size:
        cumulated_size += counts[current_idx]
        current_idx += 1

    return current_idx
