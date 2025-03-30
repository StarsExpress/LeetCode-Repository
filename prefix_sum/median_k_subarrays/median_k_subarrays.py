
def count_subarrays(numbers: list[int], k: int) -> int:  # LeetCode Q.2488.
    """
    Key: all the numbers are unique. In prefix sum, set numbers > k as 1,
    numbers < k as -1, and k as 0. A subarray with k as median will have
    prefix sum of 0 or 1 and must contain k inside it.
    """
    median_k_count, k_occurred = 0, False
    prefix_sum, sums2counts = 0, dict()

    for number in numbers:
        if number == k:
            k_occurred = True

        if number > k:
            prefix_sum += 1
        if number < k:
            prefix_sum -= 1

        if not k_occurred:  # K hasn't shown up: only update hash table.
            if prefix_sum not in sums2counts.keys():
                sums2counts.update({prefix_sum: 0})
            sums2counts[prefix_sum] += 1
            continue

        # After k shows up, only query hash table.
        for iterated_sum in {prefix_sum - 1, prefix_sum}:
            if iterated_sum in sums2counts.keys():
                median_k_count += sums2counts[iterated_sum]

        if prefix_sum in {0, 1}:  # Subarray from 0th to current idx has median k.
            median_k_count += 1

    return median_k_count
