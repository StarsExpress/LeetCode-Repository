
def binary_insert(target: int, sorted_integers: list[int] | tuple[int]):
    if len(sorted_integers) <= 0:
        return 0

    back_idx, front_idx = 0, len(sorted_integers) - 1
    while True:
        if back_idx > front_idx:
            return back_idx  # Number of ints < target, implying target's insertion idx.

        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1


def count_almost_duplicates(integers: list[int], index_diff: int, value_diff: int):  # LeetCode Q.220.
    # Find if any pair of ints within idx diff and value diff.
    if not (1 <= index_diff <= len(integers)):
        raise IndexError('Index difference must >= 1 and <= length of integers.')
    if value_diff < 0:
        raise ValueError('Value difference must >= 0.')
    if len(integers) < 2:
        return False

    window_ints = integers[: index_diff + 1]  # Window of ints within idx difference.
    window_ints.sort()  # Sort for binary insertion.
    for i in range(len(window_ints) - 1):
        if window_ints[i + 1] - window_ints[i] <= value_diff:
            return True

    back_idx, front_idx = 1, 1 + index_diff
    while True:
        if front_idx >= len(integers):  # Search reaches the end.
            return False

        window_ints.remove(integers[back_idx - 1])  # 1st int is out of window.
        newcomer = integers[front_idx]  # The int that is joining window.
        insertion_idx = binary_insert(newcomer, window_ints)

        if insertion_idx == 0:  # Newcomer < all window ints.
            if window_ints[0] - newcomer <= value_diff:
                return True

        elif insertion_idx == len(window_ints):  # Newcomer > all window ints.
            if newcomer - window_ints[-1] <= value_diff:
                return True

        else:
            if min(newcomer - window_ints[insertion_idx - 1], window_ints[insertion_idx] - newcomer) <= value_diff:
                return True

        window_ints.insert(insertion_idx, newcomer)
        back_idx += 1
        front_idx += 1
