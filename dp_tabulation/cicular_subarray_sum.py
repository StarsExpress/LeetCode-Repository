
def compute_circular_max_subarray_sum(numbers: list[int]) -> int:  # LeetCode Q.918.
    """
    Key: max "circular" sum = sum of all numbers - min subarray sum,
    where the min subarray excludes numbers at 0th & last idx.
    """
    total_sum = sum(numbers)
    incremental_subarray_sum = numbers.pop(0)
    if not numbers:  # Base case: only 1 num.
        return incremental_subarray_sum

    max_ordinary_sum = incremental_subarray_sum
    decremental_subarray_sum, min_ordinary_sum = 0, 0  # Can't contain num at 0th idx.

    total_nums = len(numbers)
    for idx, num in enumerate(numbers):
        if incremental_subarray_sum < 0:  # Incremental sum < 0: reset subarray.
            incremental_subarray_sum = 0

        incremental_subarray_sum += num
        if incremental_subarray_sum > max_ordinary_sum:
            max_ordinary_sum = incremental_subarray_sum

        if idx == total_nums - 1:  # Last num: excluded by decremental subarray.
            return max(total_sum - min_ordinary_sum, max_ordinary_sum)

        if decremental_subarray_sum > 0:  # Decremental sum > 0: reset subarray.
            decremental_subarray_sum = 0

        decremental_subarray_sum += num
        if decremental_subarray_sum < min_ordinary_sum:
            min_ordinary_sum = decremental_subarray_sum
