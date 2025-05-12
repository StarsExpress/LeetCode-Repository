from bisect import bisect_right, bisect_left


def count_range_sum(nums: list[int], lower: int, upper: int) -> int:  # LeetCode Q.327.
    prefix_sum = 0
    prefix_sums: list[int] = []

    bounded_range_sums = 0  # Count of range sums in [lower, upper].
    for num in nums:
        prefix_sum += num

        if lower <= prefix_sum <= upper:
            bounded_range_sums += 1

        # Target prefix sum x satisfies this condition.
        # prefix sum - upper <= target <= prefix sum - lower.

        right_idx = bisect_right(prefix_sums, prefix_sum - lower) - 1
        left_idx = bisect_left(prefix_sums, prefix_sum - upper)
        bounded_range_sums += right_idx + 1 - left_idx

        idx = bisect_right(prefix_sums, prefix_sum)
        prefix_sums.insert(idx, prefix_sum)

    return bounded_range_sums
