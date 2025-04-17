from bisect import bisect_right


class Calendar:  # LeetCode Q.729.
    """Book schedules without conflicts."""

    def __init__(self):
        self.booked_times = []  # Format: [inclusive start, inclusive end].

    def book(self, start: int, end: int):
        end -= 1  # Adjust to inclusive end time.

        # Idx of the first booked time w/ start > current booking start.
        idx = bisect_right(self.booked_times, [start, start])

        if idx > 0 and self.booked_times[idx - 1][1] >= start:
            return False  # Current booking causes double booking.

        if idx < len(self.booked_times) and self.booked_times[idx][0] <= end:
            return False  # Current booking causes double booking.

        self.booked_times.insert(idx, [start, end])
        return True
