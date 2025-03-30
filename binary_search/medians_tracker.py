
def track_medians(nums: list[int | float], return_sum=False, only_last_4_digits=False) -> int | list[int | float]:
    if not nums:
        return 0

    medians = []
    sorted_nums, count = [], 0  # Track count of sorted numbers.
    for num in nums:
        left_idx, right_idx = 0, count - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if sorted_nums[mid_idx] < num:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        sorted_nums.insert(left_idx, num)  # Back idx: count of sorted numbers < new num.
        count += 1  # Update count.
        if count % 2 == 1:
            medians.append(sorted_nums[count // 2])
            continue

        # For even count, median is defined as the (count / 2)th "smallest".
        medians.append(sorted_nums[(count // 2) - 1])

    if return_sum:
        medians_sum = sum(medians)
        if only_last_4_digits:
            medians_sum %= 10000
        return medians_sum
    return medians
