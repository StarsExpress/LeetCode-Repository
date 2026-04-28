
def find_uniqueness_median(nums: list[int]) -> int:  # LeetCode Q.3134.
    max_total_subarrays = len(nums) * (len(nums) + 1) // 2
    # Max total subarrays is even: take its exact half as the median.
    subarrays_median = (max_total_subarrays + 1) // 2

    nums2counts: dict[int, int] = dict()
    min_median, max_median = 1, len(nums)

    while min_median <= max_median:
        mid_median = (min_median + max_median) // 2

        subarrays_count = 0
        nums2counts.clear()  # Reset before sliding window search.
        start_idx = 0

        for end_idx, num in enumerate(nums):
            if num not in nums2counts.keys():
                nums2counts.update({num: 0})
            nums2counts[num] += 1

            while len(nums2counts) > mid_median:
                nums2counts[nums[start_idx]] -= 1
                if nums2counts[nums[start_idx]] == 0:
                    del nums2counts[nums[start_idx]]

                start_idx += 1

            # Count of subarrays ending at end idx w/ uniqueness <= mid median.
            subarrays_count += end_idx + 1 - start_idx

        if subarrays_count == subarrays_median:
            return mid_median

        elif subarrays_count < subarrays_median:
            min_median = mid_median + 1

        else:
            max_median = mid_median - 1

    return min_median
