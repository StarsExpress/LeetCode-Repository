
def find_kth_min_pair_dist(nums: list[int], k: int) -> int:  # LeetCode Q.719.
    nums.sort()
    kth_min_dist, total_nums = 0, len(nums)

    min_dist, max_dist = 0, nums[-1] - nums[0]
    while min_dist <= max_dist:
        mid_dist = (min_dist + max_dist) // 2
        
        candidate = min_dist  # Max among distances that don't exceed mid dist.

        count = 0  # Count of pairs with dist <= mid dist.
        left_idx, right_idx = 0, 0
        while left_idx < total_nums:
            while right_idx < total_nums and nums[right_idx] - nums[left_idx] <= mid_dist:
                right_idx += 1

            if nums[right_idx - 1] - nums[left_idx] > candidate:
                candidate = nums[right_idx - 1] - nums[left_idx]

            count += (right_idx - 1 - left_idx)
            left_idx += 1

        if count < k:
            min_dist = mid_dist + 1
            continue

        kth_min_dist = candidate  # Count >= k: candidate might be the kth min dist.
        if count == k:
            break
        max_dist = mid_dist - 1

    return kth_min_dist
