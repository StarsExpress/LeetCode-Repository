
def find_peak_index(mountain_array: list | tuple):  # LeetCode Q.1095.
    """Given mountain array, find its peak index."""
    back_idx, front_idx = 0, len(mountain_array) - 1
    while back_idx < front_idx:
        mid_idx = back_idx + (front_idx - back_idx) // 2

        # Peak idx within mid_idx + 1 to front_idx.
        if mountain_array[mid_idx] < mountain_array[mid_idx + 1]:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx  # Peak idx within back_idx to mid_idx.

    return back_idx
