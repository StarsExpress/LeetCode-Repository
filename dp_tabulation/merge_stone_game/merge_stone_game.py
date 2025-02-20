
def maximize_scores_difference(stones: list[int]) -> int:  # LeetCode Q.1872.
    stones_sum = sum(stones)
    max_diff = stones_sum  # Base case: when only 2 stones remain.

    # For stones count >= 3, DP starts from the 3rd rightmost stone.
    stone_idx = len(stones) - 3
    while stone_idx >= 0:
        # Current round's stones sum = stones[0] + ... + stones[idx + 1].
        stones_sum -= stones[stone_idx + 2]
        if stones_sum - max_diff > max_diff:
            max_diff = stones_sum - max_diff
        stone_idx -= 1

    return max_diff
