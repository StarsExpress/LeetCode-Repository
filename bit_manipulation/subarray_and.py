
def find_longest_subarray(numbers: list[int]) -> int:  # LeetCode Q.2419.
    max_num, total_nums = max(numbers), len(numbers)
    max_streak = current_streak = 0
    for idx, number in enumerate(numbers):
        if number == max_num:
            current_streak += 1
            if idx < total_nums - 1:  # Last idx can't skip: has to compare to max streak.
                continue

        if current_streak > max_streak:
            max_streak = current_streak
        current_streak -= current_streak

        if total_nums - idx < max_streak:  # Max streak definitely wins.
            return max_streak

    return max_streak
