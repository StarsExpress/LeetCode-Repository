
def sum_floored_pairs(nums: list[int]) -> int:  # LeetCode Q.1862.
    max_num = max(nums)
    nums2counts = [0] * (max_num + 1)  # Idx i stores count of num i. Min num >= 0.
    for num in nums:
        nums2counts[num] += 1

    prefix_counts = []
    for count in nums2counts:
        if not prefix_counts:
            prefix_counts.append(count)
            continue
        prefix_counts.append(prefix_counts[-1] + count)

    floored_pairs_sum, modulo = 0, 10 ** 9 + 7
    distinct_nums = set(nums)
    for num in distinct_nums:
        max_multiple = max_num // num
        for multiple in range(1, max_multiple + 1):
            product = num * multiple

            if multiple == max_multiple:
                count = prefix_counts[-1]

            else:
                count = prefix_counts[product + num - 1]

            count -= prefix_counts[product - 1]

            floored_pairs_sum += nums2counts[num] * multiple * count
            floored_pairs_sum %= modulo

    return floored_pairs_sum
