
def count_awaiting_days(temperatures: list[int]):  # LeetCode Q.739.
    """Count days until warmer temperature."""
    awaiting_days = [0] * len(temperatures)
    stack = [(0, temperatures[0])]  # Decreasing monotonic stack: (idx, temperature).

    for today_idx in range(1, len(temperatures)):
        if stack:
            past_idx, past_temp = stack.pop(-1)
            while past_temp < temperatures[today_idx]:  # Past temp finds a warmer future.
                awaiting_days[past_idx] += today_idx - past_idx
                if not stack:
                    break
                past_idx, past_temp = stack.pop(-1)

            if past_temp >= temperatures[today_idx]:  # Back to stack.
                stack.append((past_idx, past_temp))

        stack.append((today_idx, temperatures[today_idx]))

    return awaiting_days
