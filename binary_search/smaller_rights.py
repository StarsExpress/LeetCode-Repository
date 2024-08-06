
def count_smaller_right(target: int, sorted_integers: list[int] | tuple[int]):
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


def count_smaller_rights(integers: list[int]):  # LeetCode Q.315.
    if not integers:
        return 0

    smaller_rights = [0]  # Rightmost int has no smaller rights.
    sorted_integers = [integers.pop(-1)]  # Start from rightmost int.

    while integers:
        popped_integer = integers.pop(-1)
        smaller_right = count_smaller_right(popped_integer, sorted_integers)
        # Insert at 0 idx: iteration is from rightmost to leftmost.
        smaller_rights.insert(0, smaller_right)
        sorted_integers.insert(smaller_right, popped_integer)

    return smaller_rights
