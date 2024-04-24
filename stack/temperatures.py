
def count_awaiting_days(temperatures: list[int]):  # LeetCode Q.739.
    # Stack format: (idx, temperature).
    awaiting_days, stack = [0] * len(temperatures), [(0, temperatures[0])]

    for today_temp_idx in range(1, len(temperatures)):
        if stack:
            idx_temp_tuple = stack.pop()
            # Past temp < today temp: past temp finds a warmer future.
            while idx_temp_tuple[1] < temperatures[today_temp_idx]:
                awaiting_days[idx_temp_tuple[0]] += today_temp_idx - idx_temp_tuple[0]
                if len(stack) <= 0:
                    break
                idx_temp_tuple = stack.pop()

            # Past temp >= today temp: push it back to stack.
            if idx_temp_tuple[1] >= temperatures[today_temp_idx]:
                stack.append(idx_temp_tuple)

        # Push today temp to stack as it may be some past temp's warmer temp.
        stack.append((today_temp_idx, temperatures[today_temp_idx]))

    return awaiting_days
