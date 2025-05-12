from bisect import bisect_left


def find_sliding_window_median(nums: list[int], size: int) -> list[float]:  # LeetCode Q.480.
    window_medians: list[float] = []

    sorted_nums: list[int] = []
    median_indices: list[int] = [size // 2]
    if size % 2 == 0:
        median_indices.append((size // 2) - 1)

    left_idx = 0
    for right_idx, right_num in enumerate(nums):
        if right_idx - left_idx == size:  # Left num is out of window.
            left_num_idx = bisect_left(sorted_nums, nums[left_idx])
            sorted_nums.pop(left_num_idx)
            left_idx += 1

        right_num_idx = bisect_left(sorted_nums, right_num)
        sorted_nums.insert(right_num_idx, right_num)

        if len(sorted_nums) == size:  # Eligible to track window median.
            window_median = 0
            for median_idx in median_indices:
                window_median += sorted_nums[median_idx]

            if len(median_indices) == 2:
                window_median /= 2
            window_medians.append(window_median)

    return window_medians
