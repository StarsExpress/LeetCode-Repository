
def count_bounded_subarrays(nums: list[int], min_k: int, max_k: int):  # LeetCode Q.2444.
    bounded_subarrays_count = 0

    prev_min_idx, prev_max_idx = -1, -1

    left_idx = 0
    for right_idx, num in enumerate(nums):
        if num < min_k or num > max_k:  # Reset.
            prev_min_idx, prev_max_idx = -1, -1
            left_idx = right_idx + 1
            continue

        if num == max_k: prev_max_idx = right_idx
        if num == min_k: prev_min_idx = right_idx

        if min(prev_min_idx, prev_max_idx) >= 0:
            bounded_subarrays_count += min(prev_min_idx, prev_max_idx) + 1 - left_idx

    return bounded_subarrays_count
