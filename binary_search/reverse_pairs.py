
def count_reverse(target: int, sorted_integers: list[int] | tuple[int]):
    """Count how many integers < 0.5 * target."""
    if len(sorted_integers) <= 0:
        return 0

    insertion_idx = 0  # Target's idx into sorted integers to maintain order.
    back_idx, front_idx = 0, len(sorted_integers) - 1

    while True:  # First while: search for insertion idx.
        if back_idx > front_idx:
            insertion_idx = back_idx
            break

        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    back_idx, front_idx = 0, len(sorted_integers) - 1
    while True:  # Second while: count number of ints < 0.5 * target.
        if back_idx > front_idx:
            return back_idx, insertion_idx  # Back idx implies number of ints < 0.5 * target.

        mid_idx = (back_idx + front_idx) // 2
        if 2 * sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1


def count_reverse_pairs(integers: list[int]):  # LeetCode Q.493.
    if len(integers) <= 1:
        return 0

    reverse_pairs = 0
    sorted_integers = [integers.pop(-1)]  # Start from rightmost int.
    while integers:
        popped_int = integers.pop(-1)
        reverse_count, insertion_idx = count_reverse(popped_int, sorted_integers)
        reverse_pairs += reverse_count
        sorted_integers.insert(insertion_idx, popped_int)

    return reverse_pairs
