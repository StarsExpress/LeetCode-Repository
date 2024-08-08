
class RangesSummary:  # LeetCode Q.352.
    """Given integers stream, summarize all numbers seen so far as list of disjoint intervals."""

    def __init__(self):
        self.intervals = []  # List of lists representing intervals.

    def _binary_search(self, target: list[int]):
        if not self.intervals:
            return 0

        back_idx, front_idx = 0, len(self.intervals) - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.intervals[mid_idx] < target:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of intervals with start < int inside target.

    def add_value(self, value: int):
        if not self.intervals:
            self.intervals.insert(0, [value, value])
            return

        idx = self._binary_search([value])  # Where [value] is among intervals to maintain order.

        # First: check all cases of only one existing interval.
        if len(self.intervals) == 1:
            if value == self.intervals[0][0] - 1:  # Value = interval start - 1.
                self.intervals[0][0] -= 1  # Update interval start.
                return

            if value == self.intervals[0][1] + 1:  # Value = interval end + 1.
                self.intervals[0][1] += 1  # Update interval end.
                return

            # Value not within interval.
            if not (self.intervals[0][0] <= value <= self.intervals[0][1]):
                self.intervals.insert(idx, [value, value])
            return

        if idx == 0:  # Value <= all intervals' start.
            if value == self.intervals[0][0] - 1:  # Value = next interval start - 1.
                self.intervals[idx][0] -= 1  # Update next interval start.

            if value < self.intervals[0][0] - 1:  # Value < next interval start - 1.
                self.intervals.insert(0, [value, value])
            return

        # Value in previous interval.
        if self.intervals[idx - 1][0] <= value <= self.intervals[idx - 1][1]:
            return

        # Value <= some intervals' start, implying "next" interval's existence.
        if idx < len(self.intervals):
            # Value in next interval.
            if self.intervals[idx][0] <= value <= self.intervals[idx][1]:
                return

            # Value "connects" two intervals.
            if self.intervals[idx - 1][1] + 1 == value == self.intervals[idx][0] - 1:
                new_start = self.intervals.pop(idx - 1)[0]
                new_end = self.intervals.pop(idx - 1)[1]
                self.intervals.insert(idx - 1, [new_start, new_end])
                return

            if value == self.intervals[idx][0] - 1:  # Value = next interval start - 1.
                self.intervals[idx][0] -= 1  # Update next interval start.
                return

        if value == self.intervals[idx - 1][1] + 1:  # Value = previous interval end + 1.
            self.intervals[idx - 1][1] += 1  # Update previous interval end.
            return

        self.intervals.insert(idx, [value, value])

    def get_intervals(self):
        return self.intervals
