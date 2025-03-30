
def count_min_operations(nums: list[int]) -> int:  # LeetCode Q.2366.
    min_operations = 0
    total_nums = len(nums)
    idx = -2  # Backward idx.
    while idx >= -total_nums:
        if nums[idx] > nums[idx + 1]:  # Maximize the division by minimizing pieces to break into.
            pieces = nums[idx] // nums[idx + 1]
            if nums[idx] % nums[idx + 1] > 0:  # Have to add another piece.
                pieces += 1

            nums[idx] //= pieces
            min_operations += pieces - 1  # Conduct (pieces - 1) operations.

        idx -= 1

    return min_operations
