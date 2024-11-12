
def _count_smaller_right(target: int, sorted_integers: list[int], size: int) -> int:
    back_idx, front_idx = 0, size - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target, implying insertion idx.


def count_smaller_rights(integers: list[int]) -> list[int]:  # LeetCode Q.315.
    smaller_rights, sorted_integers = [], []
    count = 0  # Count of sorted integers.

    for integer in integers[::-1]:  # Iteration: from rightmost to leftmost.
        smaller_right = _count_smaller_right(integer, sorted_integers, count)
        smaller_rights.append(smaller_right)
        sorted_integers.insert(smaller_right, integer)
        count += 1

    return smaller_rights[::-1]  # Reverse to make order from leftmost to rightmost.
