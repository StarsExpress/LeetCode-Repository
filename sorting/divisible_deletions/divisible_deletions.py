from math import gcd


def count_min_deletions(nums: list[int], divided_nums: list[int]) -> int:  # LeetCode Q.2344.
    min_gcd = divided_nums[0]  # Base case.
    for idx in range(len(divided_nums) - 1):
        greatest_common_divisor = gcd(divided_nums[idx], divided_nums[idx + 1])
        min_gcd = gcd(min_gcd, greatest_common_divisor)
        if min_gcd == 1:  # Coprimes exist.
            break

    nums.sort()
    deletions, idx = 0, 0
    while idx < len(nums):
        if min_gcd % nums[idx] == 0:
            return deletions
        idx += 1
        deletions += 1

    return -1
