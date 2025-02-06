
def _find_rising_subsequence(
    numbers: list[int], total_numbers: int, reverse: bool = False
) -> tuple[dict, dict]:
    if reverse:
        numbers = numbers[::-1]

    indices2lens, maxs2lens = dict(), dict()
    rising_subsequence, subsequence_len = [], 0

    for idx, number in enumerate(numbers):
        # After binary search is over, back idx is insertion idx.
        left_idx, right_idx = 0, subsequence_len - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if rising_subsequence[mid_idx] < number:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        if left_idx != subsequence_len:
            rising_subsequence[left_idx] = number
            continue

        rising_subsequence.append(number)
        subsequence_len += 1

        if idx == 0:  # No need to update subsequence len for 1st iteration.
            continue

        if reverse:  # Express idx w.r.t. the original list order.
            indices2lens.update({total_numbers - 1 - idx: subsequence_len})

        else:
            indices2lens.update({idx: subsequence_len})

        maxs2lens.update({number: subsequence_len})

    return indices2lens, maxs2lens


def find_max_mountain_array(numbers: list[int]) -> int:  # LeetCode Q.1671.
    total_numbers, max_mountain_len = len(numbers), 0

    front_indices2lens, front_maxs2lengths = _find_rising_subsequence(numbers, total_numbers)
    back_indices2lens, back_maxs2lengths = _find_rising_subsequence(numbers, total_numbers, True)
    common_indices = set(front_indices2lens.keys()) & set(back_indices2lens.keys())

    for common_idx in common_indices:
        front_len = front_indices2lens[common_idx]
        back_len = back_indices2lens[common_idx]
        if front_len + back_len > max_mountain_len:
            max_mountain_len = front_len + back_len - 1  # Minus the overlapping.

    if not common_indices:  # Switch to common maximums to seek answer.
        common_maximums = set(front_maxs2lengths.keys()) & set(back_maxs2lengths.keys())

        for common_max in common_maximums:
            front_len = front_maxs2lengths[common_max]
            back_len = back_maxs2lengths[common_max]
            if front_len + back_len > max_mountain_len:
                max_mountain_len = front_len + back_len - 1  # Minus the overlapping.

    return total_numbers - max_mountain_len
