
def find_longest_rising_subsequence(numbers: list[int]) -> int:  # LeetCode Q.300.
    rising_subsequence, subsequence_len = [], 0
    for number in numbers:
        # After binary search is over, back idx is insertion idx.
        left_idx, right_idx = 0, subsequence_len - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if rising_subsequence[mid_idx] < number:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        if left_idx == subsequence_len:
            rising_subsequence.append(number)
            subsequence_len += 1

        else:
            rising_subsequence[left_idx] = number

    return subsequence_len
