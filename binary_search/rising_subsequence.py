
def find_longest_rising_subsequence(numbers: list[int]) -> int:  # LeetCode Q.300.
    rising_subsequence, subsequence_len = [], 0
    for number in numbers:
        # After binary search is over, back idx is insertion idx.
        back_idx, front_idx = 0, subsequence_len - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if rising_subsequence[mid_idx] < number:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        if back_idx == subsequence_len:
            rising_subsequence.append(number)
            subsequence_len += 1

        else:
            rising_subsequence[back_idx] = number

    return subsequence_len
