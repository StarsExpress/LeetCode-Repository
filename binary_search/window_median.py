
def binary_search(target: int, sorted_integers: list[int] | tuple[int]):
    if len(sorted_integers) <= 0:
        return 0

    back_idx, front_idx = 0, len(sorted_integers) - 1
    while True:
        if back_idx > front_idx:
            return back_idx  # Number of ints < target.

        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1


def find_sliding_window_median(integers: list[int], size: int):  # LeetCode Q.480.
    if size < 1:
        raise ValueError('Window size must >= 1.')
    if len(integers) < size:
        raise ValueError('Integers count must >= window size.')

    if size == 1:
        return integers

    odd_size = True if size % 2 == 1 else False
    sorted_window_ints, window_medians = sorted(integers[:size]), []
    for i in range(1, len(integers) - size + 2):
        if odd_size:
            last_median = sorted_window_ints[size // 2]

        else:
            last_median = (sorted_window_ints[(size // 2) - 1] + sorted_window_ints[size // 2]) / 2

        window_medians.append(last_median)
        if i == len(integers) - size + 1:  # Last iteration only needs to calculate window median.
            return window_medians

        replaced, newcomer = integers[i - 1], integers[i - 1 + size]  # Other iterations have to replace ints.
        pop_idx = binary_search(replaced, sorted_window_ints)
        sorted_window_ints.pop(pop_idx)
        insertion_idx = binary_search(newcomer, sorted_window_ints)
        sorted_window_ints.insert(insertion_idx, newcomer)