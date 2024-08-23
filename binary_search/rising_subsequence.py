
def _binary_search(target: int, sorted_integers: list[int] | tuple[int]):
    if not sorted_integers:
        return 0

    back_idx, front_idx = 0, len(sorted_integers) - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target.


def find_longest_rising_subsequence(numbers: list[int]):  # LeetCode Q.300.
    """
    When newcomer doesn't beat everybody in subsequence, do two things:
    Find out its insertion idx of subsequence. Let it replace the number at this idx.
    """
    rising_subsequence = []
    while numbers:
        newcomer = numbers.pop(0)
        newcomer_idx = _binary_search(newcomer, rising_subsequence)
        if newcomer_idx == len(rising_subsequence):  # Newcomer > everybody in subsequence.
            rising_subsequence.append(newcomer)
            continue
        rising_subsequence[newcomer_idx] = newcomer

    return len(rising_subsequence)
