from bisect import bisect_right


class RangesSummary:  # LeetCode Q.352.
    """Given integers stream, summarize all numbers seen so far as list of disjoint intervals."""

    def __init__(self):
        self.intervals = []  # Format: [inclusive left, inclusive right].

    def add_value(self, value: int):
        left, right = value, value  # Added value itself is a new range.

        idx = bisect_right(self.intervals, [left, left])  # Idx of the first range w/ start > left.
        if idx > 0 and self.intervals[idx - 1][1] + 1 >= left:  # Merge prev range.
            idx -= 1  # Insertion idx changes.
            right = max(right, self.intervals[idx][1])
            self.intervals[idx][1] = right

        else:
            self.intervals.insert(idx, [left, right])

        while idx + 1 < len(self.intervals) and self.intervals[idx + 1][0] - 1 <= right:
            right = max(right, self.intervals[idx + 1][1])
            self.intervals[idx][1] = right
            self.intervals.pop(idx + 1)  # Next range is merged.

    def get_intervals(self):
        return self.intervals
