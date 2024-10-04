
def maximize_score(card_points: list[int], k: int) -> int:  # LeetCode Q.1423.
    total_cards, points_prefix_sum = len(card_points), []
    for point in card_points:
        if not points_prefix_sum:  # 1st card.
            points_prefix_sum.append(point)
            continue
        points_prefix_sum.append(points_prefix_sum[-1] + point)

    if total_cards <= k:  # Take all the cards.
        return points_prefix_sum[-1]

    max_score, combinations = -float("inf"), k // 2
    for front_count in range(combinations + 1):
        # Collect suffix sum.
        score_1 = points_prefix_sum[-1] - points_prefix_sum[front_count - k - 1]
        if front_count > 0:  # Can collect prefix sum.
            score_1 += points_prefix_sum[front_count - 1]

        if score_1 > max_score:
            max_score = score_1

        if 2 * front_count != k:  # Score 2 and score 1 may differ.
            score_2 = points_prefix_sum[k - front_count - 1]  # Collect prefix sum.
            if front_count < combinations:  # Can collect suffix sum.
                score_2 += points_prefix_sum[-1] - points_prefix_sum[-front_count - 1]

            if score_2 > max_score:
                max_score = score_2

    return max_score
