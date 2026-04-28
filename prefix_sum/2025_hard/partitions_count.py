
def count_max_partitions(nums: list[int], k: int) -> int:  # LeetCode Q.2025.
    total_sum, total_nums = sum(nums), len(nums)

    max_partition_ways, prefix_sum = 0, nums[0]
    for pivot in range(1, total_nums):
        if 2 * prefix_sum == total_sum:
            max_partition_ways += 1  # A natural pivot.
        prefix_sum += nums[pivot]

    right_side_diffs: dict[int, int] = dict()
    suffix_sum = 0
    for idx, num in enumerate(nums[::-1][:-1]):
        suffix_sum += num
        diff = total_sum - 2 * suffix_sum  # Diff = prefix sum - suffix sum.
        if diff not in right_side_diffs.keys():
            right_side_diffs[diff] = 0
        right_side_diffs[diff] += 1

    left_side_diffs: dict[int, int] = dict()
    prefix_sum = 0
    for idx, num in enumerate(nums):
        partition_ways = 0

        right_change = num - k
        if right_change in right_side_diffs.keys():
            partition_ways += right_side_diffs[right_change]

        left_change = k - num
        if left_change in left_side_diffs.keys():
            partition_ways += left_side_diffs[left_change]

        if partition_ways > max_partition_ways:
            max_partition_ways = partition_ways

        prefix_sum += num
        if idx > 0:  # Suffix doesn't cover num at 0th idx.
            suffix_sum -= num

        diff = prefix_sum - suffix_sum  # Diff = prefix sum - suffix sum.
        if diff not in left_side_diffs.keys():
            left_side_diffs[diff] = 0
        left_side_diffs[diff] += 1

        if diff in right_side_diffs.keys():
            right_side_diffs[diff] -= 1

    return max_partition_ways
