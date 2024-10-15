from bisect import *
from operator import itemgetter


class IntervalsCounter:  # LeetCode Q.2276.
    def __init__(self) -> None:
        # Initialize intervals as below to handle edge cases.
        self.intervals = [(-float("inf"), -float("inf")), (float("inf"), float("inf"))]
        self.total_coverage = 0

    def add_interval(self, left: int, right: int) -> None:
        # Find leftmost position for insertion of the new interval.
        # Use left - 1: interval coverage is inclusive.
        left_idx = bisect_left(self.intervals, left - 1, key=itemgetter(1))
        merged_left = min(self.intervals[left_idx][0], left)

        # Find rightmost position for insertion of the new interval.
        # Use right + 1: interval coverage is inclusive.
        right_idx = bisect_right(self.intervals, right + 1, key=itemgetter(0))
        merged_right = max(self.intervals[right_idx - 1][1], right)

        # Deduct the coverage of intervals that will be replaced by merged interval.
        for idx in range(left_idx, right_idx):
            self.total_coverage -= (self.intervals[idx][1] + 1 - self.intervals[idx][0])

        self.total_coverage += merged_right + 1 - merged_left
        self.intervals[left_idx: right_idx] = [(merged_left, merged_right)]

    def count_coverage(self) -> int:
        return self.total_coverage
