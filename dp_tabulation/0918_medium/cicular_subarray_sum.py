
def compute_circular_max_subarray_sum(nums: list[int]) -> int:  # LeetCode Q.918.
    """
    Key: max "circular" sum = sum of all numbers - min subarray sum,
    where the min subarray excludes numbers at 0th & last idx.
    """
    array_total_sum = 0
    max_num = nums[0]

    pos_subarray_sum = 0
    max_pos_sum = 0

    neg_subarray_sum = 0
    min_neg_sum = 0

    for num in nums:
        if num > max_num: max_num = num

        array_total_sum += num

        pos_subarray_sum += num
        if pos_subarray_sum > max_pos_sum:
            max_pos_sum = pos_subarray_sum

        if pos_subarray_sum <= 0:  # Positive sum <= 0: reset subarray.
            pos_subarray_sum = 0
        
        neg_subarray_sum += num
        if neg_subarray_sum < min_neg_sum:
            min_neg_sum = neg_subarray_sum

        if neg_subarray_sum >= 0:  # Negative sum >= 0: reset subarray.
            neg_subarray_sum = 0

    if max_num <= 0: return max_num  # All numbers are non-positive.

    if min_neg_sum >= 0: return array_total_sum  # All numbers are non-negative.

    return max(array_total_sum - min_neg_sum, max_pos_sum)
