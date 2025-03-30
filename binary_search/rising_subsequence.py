
def find_longest_rising_subsequence(nums: list[int]) -> int:  # LeetCode Q.300.
    rising_subsequence, subsequence_len = [], 0
    for num in nums:
        # After binary search is over, back idx is insertion idx.
        left_idx, right_idx = 0, subsequence_len - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if rising_subsequence[mid_idx] < num:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        if left_idx == subsequence_len:
            rising_subsequence.append(num)
            subsequence_len += 1

        else:
            rising_subsequence[left_idx] = num

    return subsequence_len
