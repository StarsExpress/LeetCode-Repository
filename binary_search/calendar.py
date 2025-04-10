
class Calendar:  # LeetCode Q.729.
    """Book schedules without conflicts."""

    def __init__(self):
        self.booked_times, self.booked_count = [], 0

    def _binary_search(self, time: int):
        left_idx, right_idx = 0, self.booked_count - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if self.booked_times[mid_idx] <= time:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        return left_idx  # Number of booked times <= time is insertion idx.

    def book(self, start: int, end: int):
        start_idx = self._binary_search(start)
        # Already booked times are pairs. Odd start idx means booking conflict.
        if start_idx & 1:
            return False

        end_idx = self._binary_search(end)
        if start_idx == end_idx:
            self.booked_times.insert(start_idx, start)
            self.booked_count += 1
            self.booked_times.insert(self._binary_search(end), end)
            self.booked_count += 1
            return True

        if self.booked_times[start_idx] == self.booked_times[end_idx - 1]:
            if (self.booked_times[start_idx] <= start) | (end <= self.booked_times[end_idx - 1]):
                self.booked_times.insert(start_idx, start)
                self.booked_count += 1
                self.booked_times.insert(self._binary_search(end), end)
                self.booked_count += 1
                return True

        return False
