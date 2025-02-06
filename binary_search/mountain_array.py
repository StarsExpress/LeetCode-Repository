
def find_peak_index(mountain_array: list | tuple) -> int:  # LeetCode Q.1095.
    """Given mountain array, find its peak index."""
    left_idx, right_idx = 0, len(mountain_array) - 1
    while left_idx < right_idx:
        mid_idx = left_idx + (right_idx - left_idx) // 2

        # Peak idx within mid_idx + 1 to right_idx.
        if mountain_array[mid_idx] < mountain_array[mid_idx + 1]:
            left_idx = mid_idx + 1
            continue
        right_idx = mid_idx  # Peak idx within left_idx to mid_idx.

    return left_idx
