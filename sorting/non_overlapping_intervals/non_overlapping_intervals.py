
def erase_overlapping_intervals(intervals: list[list[int]]) -> int:  # LeetCode Q.435.
    initial_size = len(intervals)
    intervals.sort()
    final_intervals: list[list[int]] = [intervals.pop(0)]
    for start, end in intervals:
        if final_intervals[-1][1] <= start:  # New interval can attach next to last interval.
            final_intervals.append([start, end])

        if end < final_intervals[-1][1]:
            # New interval is entirely inside last interval.
            final_intervals[-1] = [start, end]  # Replace last interval with new interval.

    return initial_size - len(final_intervals)
