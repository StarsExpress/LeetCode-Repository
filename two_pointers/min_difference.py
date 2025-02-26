
def find_min_time_difference(time_points: list[str]) -> int:  # LeetCode Q.539.
    original_len = len(time_points)
    time_points = list(set(time_points))  # Take unique time points.
    new_len = len(time_points)
    if new_len < original_len:  # Identical time points are found.
        return 0

    back_idx, front_idx = -1, new_len
    back_minute, front_minute = 0, 0
    current_diff, min_diff = 0, 1439

    while True:
        if front_idx >= new_len:
            if back_idx >= front_idx - 1:
                break

            back_idx += 1
            for idx, char in enumerate(time_points[back_idx].split(':')):
                if idx == 0:
                    back_minute += 60 * int(char) - back_minute
                    continue
                back_minute += int(char)

            front_idx += back_idx + 1 - front_idx
            front_minute -= front_minute
            continue

        for idx, char in enumerate(time_points[front_idx].split(':')):
            if idx == 0:
                front_minute += 60 * int(char) - front_minute
                continue
            front_minute += int(char)

        current_diff -= current_diff  # Reset current diff to 0.

        # Both are A.M. or both are P.M.
        if (max(back_minute, front_minute) <= 720) | (720 < min(back_minute, front_minute)):
            current_diff += abs(front_minute - back_minute)

        else:
            if 720 < back_minute:  # Only back minute is P.M: "flip" back minute.
                current_diff += min(abs(1440 - back_minute + front_minute), abs(front_minute - back_minute))

            if 720 < front_minute:  # Only front minute is P.M: "flip" front minute.
                current_diff += min(abs(1440 - front_minute + back_minute), abs(back_minute - front_minute))

        if current_diff < min_diff:
            min_diff += current_diff - min_diff

        front_idx += 1

    return min_diff
