
def _binary_search(target: int, sorted_integers: list[int], size: int) -> int:
    left_idx, right_idx = 0, size - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_integers[mid_idx] < target:
            left_idx = mid_idx + 1
            continue
        right_idx = mid_idx - 1

    return left_idx  # Number of ints < target, implying insertion idx.


def count_almost_duplicates(integers: list[int], idx_diff: int, val_diff: int) -> bool:  # LeetCode Q.220.
    """Find if any pair of ints within idx diff and value diff."""
    total_nums = len(integers)
    window_size = min(total_nums, idx_diff + 1)
    window_ints = integers[: window_size]  # Window of ints within idx difference.
    window_ints.sort()  # Sort for binary search.

    for i in range(window_size - 1):
        if window_ints[i + 1] - window_ints[i] <= val_diff:
            return True

    current_idx = 1
    while current_idx + idx_diff < total_nums:
        pop_idx = _binary_search(integers[current_idx - 1], window_ints, window_size)
        window_ints.pop(pop_idx)  # Window's 1st int is out.
        window_size -= 1

        newcomer = integers[current_idx + idx_diff]  # The int that is joining window.
        insertion_idx = _binary_search(newcomer, window_ints, window_size)

        if insertion_idx == 0:  # Newcomer < all window ints.
            if window_ints[0] - newcomer <= val_diff:
                return True

        if insertion_idx == window_size:  # Newcomer > all window ints.
            if newcomer - window_ints[-1] <= val_diff:
                return True

        if 0 < insertion_idx < window_size:
            if min(newcomer - window_ints[insertion_idx - 1], window_ints[insertion_idx] - newcomer) <= val_diff:
                return True

        window_ints.insert(insertion_idx, newcomer)
        window_size += 1
        current_idx += 1

    return False
