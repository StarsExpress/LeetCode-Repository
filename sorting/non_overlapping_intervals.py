
def erase_overlapping_intervals(intervals: list[list[int]]) -> int:  # LeetCode Q.435.
    starts2ends: dict[int, int] = dict()
    for start, end in intervals:
        if start not in starts2ends.keys():
            starts2ends.update({start: end})
        if end < starts2ends[start]:  # Always take the smaller end for a given start.
            starts2ends.update({start: end})

    filtered_intervals: list[tuple] = list(starts2ends.items())
    filtered_intervals.sort(key=lambda x: x[0])  # Sort by ascending starts.

    final_intervals: list[tuple] = [filtered_intervals.pop(0)]
    for start, end in filtered_intervals:
        if final_intervals[-1][0] < end < final_intervals[-1][1]:
            # New interval is entirely inside last interval.
            final_intervals[-1] = start, end  # Replace last interval with new interval.

        if final_intervals[-1][1] <= start:  # New interval can attach next to last interval.
            final_intervals.append((start, end))

    return len(intervals) - len(final_intervals)
