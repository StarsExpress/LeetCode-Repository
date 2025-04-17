
def count_k_sum_subarrays(nums: list[int], target: int) -> int:  # LeetCode Q.560.
    total_subarrays = 0
    prefix_sum, prefix_sums2counts = 0, dict()
    for num in nums:
        prefix_sum += num
        if prefix_sum == target:  # Subarray from idx 0 to current idx.
            total_subarrays += 1

        if prefix_sum - target in prefix_sums2counts.keys():  # Subarrays from idx i > 0 to current idx.
            total_subarrays += prefix_sums2counts[prefix_sum - target]
        
        if prefix_sum not in prefix_sums2counts.keys():
            prefix_sums2counts.update({prefix_sum: 0})
        prefix_sums2counts[prefix_sum] += 1
    
    return total_subarrays
