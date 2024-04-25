
def count_awaiting_days(temperatures: list[int]):  # LeetCode Q.739: count days until warmer temperature.
    # Monotonic-decreasing stack: (idx, temperature).
    awaiting_days, stack = [0] * len(temperatures), [(0, temperatures[0])]

    for today_temp_idx in range(1, len(temperatures)):
        if stack:
            idx_temp_tuple = stack.pop(-1)
            # Past temp < today temp: past temp finds a warmer future.
            while idx_temp_tuple[1] < temperatures[today_temp_idx]:
                awaiting_days[idx_temp_tuple[0]] += today_temp_idx - idx_temp_tuple[0]
                if len(stack) <= 0:
                    break
                idx_temp_tuple = stack.pop(-1)

            if idx_temp_tuple[1] >= temperatures[today_temp_idx]:  # Past temp >= today temp: back to stack.
                stack.append(idx_temp_tuple)

        stack.append((today_temp_idx, temperatures[today_temp_idx]))

    return awaiting_days
