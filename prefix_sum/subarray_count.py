
def count_k_sum_subarrays(numbers: list[int], target: int) -> int:  # LeetCode Q.560.
    subarrays_count = 0
    prefix_sum, prefix_sums_table = 0, dict()
    for current_idx, number in enumerate(numbers):
        if number == target:  # Case 1: current number = target.
            subarrays_count += 1

        prefix_sum += number
        if prefix_sum not in prefix_sums_table.keys():
            prefix_sums_table.update(
                {  # Track last 2 "end indices" for each occurred prefix sum.
                    prefix_sum: {"count": 0, "last_2_indices": []}
                }
            )

        if prefix_sums_table[prefix_sum]["count"] >= 2:  # Only need last 2 end indices.
            prefix_sums_table[prefix_sum]["last_2_indices"].pop(0)
        prefix_sums_table[prefix_sum]["last_2_indices"].append(current_idx)
        prefix_sums_table[prefix_sum]["count"] += 1

        # Case 2: current number isn't the 1st number, and has prefix sum = target.
        if current_idx > 0 and prefix_sum == target:
            subarrays_count += 1

        # Case 3: count "complements" for current prefix sum.
        difference = prefix_sum - target
        if difference in prefix_sums_table.keys():
            subarrays_count += prefix_sums_table[difference]["count"]
            # Repeated counts: last 2 end indices >= current_idx - 1.
            for last_2_idx in prefix_sums_table[difference]["last_2_indices"]:
                if last_2_idx >= current_idx - 1:
                    subarrays_count -= 1

    return subarrays_count
