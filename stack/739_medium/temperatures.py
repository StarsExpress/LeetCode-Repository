
def count_awaiting_days(temperatures: list[int]) -> list[int]:  # LeetCode Q.739.
    total_temp = len(temperatures)
    # Decreasing monotonic stack: (idx, temperature).
    awaiting_days, stack = [0] * total_temp, [(0, temperatures[0])]

    for today_idx in range(1, total_temp):
        # Past temp finds a warmer future.
        while stack and stack[-1][1] < temperatures[today_idx]:
            past_idx, _ = stack.pop(-1)
            awaiting_days[past_idx] += today_idx - past_idx

        stack.append((today_idx, temperatures[today_idx]))

    return awaiting_days
