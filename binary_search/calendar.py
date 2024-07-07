
class Calendar:  # LeetCode Q.729.
    """Book schedules without conflicts."""

    def __init__(self):
        self.booked_times, self.booked_count = [], 0

    def binary_search(self, time: int):
        if self.booked_count <= 0:
            return 0

        back_idx, front_idx = 0, self.booked_count - 1
        while True:
            if back_idx > front_idx:
                return back_idx  # Number of booked times <= time is insertion idx.

            mid_idx = (back_idx + front_idx) // 2
            if self.booked_times[mid_idx] <= time:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

    def book(self, start: int, end: int):
        start_idx = self.binary_search(start)
        # Already booked times are pairs. Odd start idx means booking conflict.
        if start_idx & 1:
            return False

        end_idx = self.binary_search(end)
        if start_idx == end_idx:
            self.booked_times.insert(start_idx, start)
            self.booked_count += 1
            self.booked_times.insert(self.binary_search(end), end)
            self.booked_count += 1
            return True

        if self.booked_times[start_idx] == self.booked_times[end_idx - 1]:
            if (self.booked_times[start_idx] <= start) | (end <= self.booked_times[end_idx - 1]):
                self.booked_times.insert(start_idx, start)
                self.booked_count += 1
                self.booked_times.insert(self.binary_search(end), end)
                self.booked_count += 1
                return True

        return False
