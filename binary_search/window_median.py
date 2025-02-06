
def _binary_search(target: int, sorted_integers: list[int], size: int) -> int:
    left_idx, right_idx = 0, size - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_integers[mid_idx] < target:
            left_idx = mid_idx + 1
            continue
        right_idx = mid_idx - 1

    return left_idx  # Number of ints < target.


def find_sliding_window_median(integers: list[int], size: int) -> list[float]:  # LeetCode Q.480.
    if size == 1:
        return integers

    odd_size = True if size % 2 == 1 else False
    total_ints = len(integers)
    sorted_window, window_medians = sorted(integers[:size]), []
    for i in range(1, total_ints - size + 2):
        if odd_size:
            last_median = sorted_window[size // 2]

        else:
            last_median = (sorted_window[(size // 2) - 1] + sorted_window[size // 2]) / 2

        window_medians.append(last_median)
        if i < total_ints - size + 1:  # Non-last iterations have to replace ints.
            replaced, newcomer = integers[i - 1], integers[i - 1 + size]
            replaced_idx = _binary_search(replaced, sorted_window, size)
            sorted_window.pop(replaced_idx)

            newcomer_idx = _binary_search(newcomer, sorted_window, size - 1)
            sorted_window.insert(newcomer_idx, newcomer)

    return window_medians
