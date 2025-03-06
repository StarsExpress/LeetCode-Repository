
def find_1st_missing_positive(nums: list[int]) -> int:  # LeetCode Q.41.
    nums = [num for num in nums if num > 0]
    total_nums = len(nums)
    for num in nums:
        idx = abs(num) - 1
        if idx < total_nums and 0 < nums[idx]:
            nums[idx] *= -1

    for idx, num in enumerate(nums):
        if num > 0:
            return idx + 1

    return total_nums + 1
