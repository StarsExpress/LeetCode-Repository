
def maximize_scores_difference(stones: list[int]) -> int:  # LeetCode Q.1872.
    prefix_sum = sum(stones)

    # Base case: Alice merges everything as the only attempt.
    max_score_diff = prefix_sum

    prefix_sum -= stones[-1]

    for idx in range(len(stones) - 2, 0, -1):
        if prefix_sum - max_score_diff > max_score_diff:
            max_score_diff = prefix_sum - max_score_diff

        prefix_sum -= stones[idx]

    return max_score_diff
