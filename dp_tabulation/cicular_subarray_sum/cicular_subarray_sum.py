
def compute_circular_max_subarray_sum(nums: list[int]) -> int:  # LeetCode Q.918.
    """
    Key: max "circular" sum = sum of all numbers - min subarray sum,
    where the min subarray excludes numbers at 0th & last idx.
    """
    array_total_sum = 0
    max_num = float("-inf")

    pos_subarray_sum = 0
    max_pos_sum = 0

    neg_subarray_sum = 0
    min_neg_sum = 0

    total_nums = len(nums)

    for idx, num in enumerate(nums):
        array_total_sum += num

        if num > max_num: max_num = num
        
        if pos_subarray_sum <= 0:  # Positive sum <= 0: reset subarray.
            pos_subarray_sum = 0
    
        pos_subarray_sum += num
        if pos_subarray_sum > max_pos_sum: max_pos_sum = pos_subarray_sum
        
        # Front and last nums are excluded by negative sum subarray.
        if 0 < idx < total_nums - 1:
            if neg_subarray_sum >= 0:  # Negative sum >= 0: reset subarray.
                neg_subarray_sum = 0

            neg_subarray_sum += num
            if neg_subarray_sum < min_neg_sum: min_neg_sum = neg_subarray_sum

    if max_num <= 0: return max_num  # All numbers are not positive.

    return max(array_total_sum - min_neg_sum, max_pos_sum)
