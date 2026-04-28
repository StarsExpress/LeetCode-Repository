
def _count_limited_subarrays(nums: list[int], distinction_limit: int) -> int:
    total_subarrays = 0

    nums2counts, start_idx = dict(), 0
    for end_idx, num in enumerate(nums):
        if num not in nums2counts.keys():
            nums2counts.update({num: 0})
        nums2counts[num] += 1

        while len(nums2counts) > distinction_limit:
            nums2counts[nums[start_idx]] -= 1
            if nums2counts[nums[start_idx]] == 0:
                del nums2counts[nums[start_idx]]
            start_idx += 1

        total_subarrays += end_idx - start_idx + 1

    return total_subarrays

def count_k_distinct_subarrays(nums: list[int], k: int) -> int:  # LeetCode Q.992.
    return _count_limited_subarrays(nums, k) - _count_limited_subarrays(nums, k - 1)
