
def _count_reverse(target: int, sorted_integers: list[int], size: int) -> tuple[int, int]:
    """Count how many integers < 0.5 * target. Beware of negative integers."""
    left_idx, right_idx = 0, size - 1
    while left_idx <= right_idx:  # First while: search for insertion idx.
        mid_idx = (left_idx + right_idx) // 2
        if sorted_integers[mid_idx] < target:
            left_idx = mid_idx + 1
            continue
        right_idx = mid_idx - 1

    insertion_idx = left_idx

    left_idx, right_idx = 0, size - 1  # Front idx starts at size - 1: in case of negative ints.
    while left_idx <= right_idx:  # Second while: count the number of ints < 0.5 * target.
        mid_idx = (left_idx + right_idx) // 2
        if 2 * sorted_integers[mid_idx] < target:
            left_idx = mid_idx + 1
            continue
        right_idx = mid_idx - 1

    return left_idx, insertion_idx  # Back idx implies the number of ints < 0.5 * target.


def count_reverse_pairs(integers: list[int]) -> int:  # LeetCode Q.493.
    reverse_pairs, sorted_integers = 0, []
    count = 0  # Count of sorted integers.
    for integer in integers[::-1]:  # Iteration: from rightmost to leftmost.
        reverse_count, insertion_idx = _count_reverse(integer, sorted_integers, count)
        reverse_pairs += reverse_count
        sorted_integers.insert(insertion_idx, integer)
        count += 1

    return reverse_pairs
