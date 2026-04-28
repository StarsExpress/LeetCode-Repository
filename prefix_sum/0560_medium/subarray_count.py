
def count_k_sum_subarrays(nums: list[int], k: int) -> int:  # LeetCode Q.560.
    prefix_sum_counts: dict[int, int] = dict()
    prefix_sum = 0

    k_sum_subarrays_count = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_sum_counts.keys():
            k_sum_subarrays_count += prefix_sum_counts[prefix_sum - k]

        if prefix_sum == k: k_sum_subarrays_count += 1

        if prefix_sum not in prefix_sum_counts.keys():
            prefix_sum_counts.update({prefix_sum: 0})
        prefix_sum_counts[prefix_sum] += 1

    return k_sum_subarrays_count
