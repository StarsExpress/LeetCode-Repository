
def split_triplets(nums: list[int]) -> list[int]:  # LeetCode Q.927.
    total_sum = sum(nums)
    if total_sum % 3 != 0:  # Base case.
        return [-1, -1]
    if total_sum == 0:  # Base case.
        return [0, 2]

    total_nums, one_third = len(nums), total_sum // 3
    encountered_ones, ending_zeros = 0, 0
    num_1_last_1_idx, num_2_first_1_idx = None, None
    num_2_last_1_idx, num_3_first_1_idx = None, None

    for idx, num in enumerate(nums):
        if num == 1:
            encountered_ones += 1

            if encountered_ones == one_third:
                num_1_last_1_idx = idx

            if encountered_ones == one_third + 1:
                num_2_first_1_idx = idx

            if encountered_ones == 2 * one_third:
                num_2_last_1_idx = idx

            if encountered_ones == 2 * one_third + 1:
                num_3_first_1_idx = idx

            if encountered_ones == total_sum:  # Location of the last 1.
                ending_zeros += total_nums - 1 - idx
                break

    num_2_last_1_idx += ending_zeros
    if num_2_last_1_idx >= num_3_first_1_idx:
        return [-1, -1]

    num_1_last_1_idx += ending_zeros
    if num_1_last_1_idx >= num_2_first_1_idx:
        return [-1, -1]

    split_1_idx, split_2_idx = num_1_last_1_idx, num_2_last_1_idx + 1

    num_1 = int("".join(str(num) for num in nums[:split_1_idx + 1]), 2)
    num_2 = int("".join(str(num) for num in nums[split_1_idx + 1: split_2_idx]), 2)
    if num_1 != num_2:
        return [-1, -1]

    num_3 = int("".join(str(num) for num in nums[split_2_idx:]), 2)
    if num_2 != num_3:
        return [-1, -1]
    return [split_1_idx, split_2_idx]
