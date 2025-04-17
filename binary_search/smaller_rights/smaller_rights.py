from bisect import bisect_right


def count_smaller_rights(nums: list[int]) -> list[int]:  # LeetCode Q.315.
    smaller_rights, sorted_nums = [], []

    for num in nums[::-1]:  # Iteration: from rightmost to leftmost.
        # Idx of the 1st right side sorted num > current num - 1.
        idx = bisect_right(sorted_nums, num - 1)

        smaller_rights.append(idx)
        sorted_nums.insert(idx, num)

    return smaller_rights[::-1]  # Reverse to make order from leftmost to rightmost.
