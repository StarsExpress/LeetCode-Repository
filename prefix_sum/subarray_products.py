
def count_subarray_products(positive_nums: list[int], k: int) -> int:  # LeetCode Q.713.
    total_subarrays = 0
    subarray_product = 1
    start_idx = 0
    for end_idx, num in enumerate(positive_nums):
        subarray_product *= num
        while subarray_product >= k and start_idx <= end_idx:
            subarray_product /= positive_nums[start_idx]
            start_idx += 1

        if start_idx <= end_idx:
            total_subarrays += end_idx + 1 - start_idx

    return total_subarrays
