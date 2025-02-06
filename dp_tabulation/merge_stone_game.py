
def maximize_scores_difference(stones: list[int]) -> int:  # LeetCode Q.1872.
    values_prefix_sum = sum(stones)
    max_diff = values_prefix_sum  # Base case: when only 2 stones remain.
    remaining_stones, total_stones = 2, len(stones)
    while remaining_stones < total_stones:
        # Scores diff of moving the leftmost (1 + total - remaining) stones.
        values_prefix_sum -= stones[1 + total_stones - remaining_stones]
        scores_diff = values_prefix_sum - max_diff
        if scores_diff > max_diff:
            max_diff = scores_diff

        remaining_stones += 1

    return max_diff
