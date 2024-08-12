
def find_max_score(numbers: list[int], k: int):  # LeetCode Q.1793.
    """
    Score of subarray (i, j) is min(numbers[i], ..., numbers[j]) * (j - i + 1).
    A good subarray is a subarray where i <= k <= j.
    """
    numbers_count = len(numbers)
    subarray_min = numbers[k]
    max_score = numbers[k]  # Base case: subarray of only number at kth idx.

    start_idx, end_idx = k, k  # Search until one side is unsearchable.
    while start_idx > 0 and end_idx < numbers_count - 1:
        if numbers[end_idx + 1] >= numbers[start_idx - 1]:  # Extend right side.
            subarray_min = min(subarray_min, numbers[end_idx + 1])
            end_idx += 1

        else:  # Extend left side.
            subarray_min = min(subarray_min, numbers[start_idx - 1])
            start_idx -= 1

        if subarray_min * (end_idx - start_idx + 1) > max_score:
            max_score = subarray_min * (end_idx - start_idx + 1)

    while start_idx > 0:  # Left side is still searchable.
        subarray_min = min(subarray_min, numbers[start_idx - 1])
        start_idx -= 1
        if subarray_min * (end_idx - start_idx + 1) > max_score:
            max_score = subarray_min * (end_idx - start_idx + 1)

    while end_idx < numbers_count - 1:  # Right side is still searchable.
        subarray_min = min(subarray_min, numbers[end_idx + 1])
        end_idx += 1
        if subarray_min * (end_idx - start_idx + 1) > max_score:
            max_score = subarray_min * (end_idx - start_idx + 1)

    return max_score
