
class RangesSummary:  # LeetCode Q.352.
    """Given a stream of integers, summarize all numbers seen so far as list of disjoint intervals."""

    def __init__(self):
        self.intervals = []  # List of lists representing intervals.

    def binary_insert(self, target: list[int]):
        if len(self.intervals) <= 0:
            return 0

        back_idx, front_idx = 0, len(self.intervals) - 1
        while True:
            if back_idx > front_idx:
                return back_idx  # Number of intervals with start < target's int.

            mid_idx = (back_idx + front_idx) // 2
            if self.intervals[mid_idx] < target:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

    def add_value(self, value: int):
        if len(self.intervals) == 0:
            self.intervals.insert(0, [value, value])
            return

        idx = self.binary_insert([value])  # Where [value] is among intervals to maintain order.
        if len(self.intervals) == 1:  # First finish cases of only one existing interval.
            if value == self.intervals[0][0] - 1:  # Value = interval start - 1.
                self.intervals[0][0] -= 1  # Update interval start.
                return

            if value == self.intervals[0][1] + 1:  # Value = interval end + 1.
                self.intervals[0][1] += 1  # Update interval end.
                return

            if not (self.intervals[0][0] <= value <= self.intervals[0][1]):  # Value not within interval.
                self.intervals.insert(idx, [value, value])
            return

        if idx == 0:  # Value <= all intervals' start.
            if value == self.intervals[0][0] - 1:  # Value = next interval start - 1.
                self.intervals[idx][0] -= 1  # Update next interval start.

            if value < self.intervals[0][0] - 1:  # Value < next interval start - 1.
                self.intervals.insert(0, [value, value])
            return

        if self.intervals[idx - 1][0] <= value <= self.intervals[idx - 1][1]:  # Value in previous interval.
            return

        if idx < len(self.intervals):  # Value <= some intervals' start, implying "next" interval's existence.
            if self.intervals[idx][0] <= value <= self.intervals[idx][1]:  # Value in next interval.
                return

            if self.intervals[idx - 1][1] + 1 == value == self.intervals[idx][0] - 1:  # Value "connects" two intervals.
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
