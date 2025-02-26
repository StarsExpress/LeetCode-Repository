
def find_max_score(nums: list[int], k: int) -> int:  # LeetCode Q.1793.
    """
    Score of subarray (i, j) is min(nums[i], ..., num[j]) * (j - i + 1).
    A good subarray is a subarray where i <= k <= j.
    """
    total_nums = len(nums)
    subarray_min = nums[k]
    max_score = nums[k]  # Base case: subarray of only num at kth idx.

    start_idx, end_idx = k, k  # Search until one side is unsearchable.
    while start_idx > 0 and end_idx < total_nums - 1:
        if nums[end_idx + 1] >= nums[start_idx - 1]:  # Extend right side.
            subarray_min = min(subarray_min, nums[end_idx + 1])
            end_idx += 1

        else:  # Extend left side.
            subarray_min = min(subarray_min, nums[start_idx - 1])
            start_idx -= 1

        if subarray_min * (end_idx - start_idx + 1) > max_score:
            max_score = subarray_min * (end_idx - start_idx + 1)

    while start_idx > 0:  # Left side is still searchable.
        subarray_min = min(subarray_min, nums[start_idx - 1])
        start_idx -= 1
        if subarray_min * (end_idx - start_idx + 1) > max_score:
            max_score = subarray_min * (end_idx - start_idx + 1)

    while end_idx < total_nums - 1:  # Right side is still searchable.
        subarray_min = min(subarray_min, nums[end_idx + 1])
        end_idx += 1
        if subarray_min * (end_idx - start_idx + 1) > max_score:
            max_score = subarray_min * (end_idx - start_idx + 1)

    return max_score
