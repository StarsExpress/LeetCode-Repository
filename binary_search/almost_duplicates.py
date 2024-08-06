
def binary_search(target: int, sorted_integers: list[int] | tuple[int]):
    if not sorted_integers:
        return 0

    back_idx, front_idx = 0, len(sorted_integers) - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target, implying insertion idx.


def count_almost_duplicates(integers: list[int], idx_diff: int, val_diff: int):  # LeetCode Q.220.
    """Find if any pair of ints within idx diff and value diff."""

    if not (1 <= idx_diff <= len(integers)):
        raise IndexError("Index difference must >= 1 and <= length of integers.")
    if val_diff < 0:
        raise ValueError("Value difference must >= 0.")
    if len(integers) < 2:
        return False

    window_ints = integers[: idx_diff + 1]  # Window of ints within idx diff.
    window_ints.sort()  # Sort for binary insertion.

    for i in range(len(window_ints) - 1):
        if window_ints[i + 1] - window_ints[i] <= val_diff:
            return True

    back_idx, front_idx = 1, 1 + idx_diff
    while True:
        if front_idx >= len(integers):  # Search reaches the end.
            return False

        pop_idx = binary_search(integers[back_idx - 1], window_ints)
        window_ints.pop(pop_idx)  # Window's 1st int is out.

        newcomer = integers[front_idx]  # The int that is joining window.
        newcomer_idx = binary_search(newcomer, window_ints)

        if newcomer_idx == 0:  # Newcomer < all window ints.
            if window_ints[0] - newcomer <= val_diff:
                return True

        elif newcomer_idx == len(window_ints):  # Newcomer > all window ints.
            if newcomer - window_ints[-1] <= val_diff:
                return True

        else:
            if min(
                    newcomer - window_ints[newcomer_idx - 1],
                    window_ints[newcomer_idx] - newcomer,
            ) <= val_diff:
                return True

        window_ints.insert(newcomer_idx, newcomer)
        back_idx += 1
        front_idx += 1
