
def find_min_unsorted_subarray(nums: list[int]) -> int:  # LeetCode Q.581.
    first_misplaced_idx = None
    last_misplaced_idx = None
    for idx, num in enumerate(nums[:-1]):
        if num > nums[idx + 1]:
            if first_misplaced_idx is None:
                first_misplaced_idx = idx

            last_misplaced_idx = idx + 1

    if first_misplaced_idx is None:
        return 0

    misplaced_range_min = float("inf")
    misplaced_range_max = -float("inf")
    for idx in range(first_misplaced_idx, last_misplaced_idx + 1):
        if nums[idx] < misplaced_range_min:
            misplaced_range_min = nums[idx]
        if nums[idx] > misplaced_range_max:
            misplaced_range_max = nums[idx]

    for idx in range(first_misplaced_idx):
        if nums[idx] > misplaced_range_min:
            first_misplaced_idx = idx
            break

    for idx in range(len(nums) - 1, last_misplaced_idx, -1):
        if nums[idx] < misplaced_range_max:
            last_misplaced_idx = idx
            break

    return last_misplaced_idx + 1 - first_misplaced_idx
