
class DataStream:  # LeetCode Q.2526.
    """Check if last k integers all equal certain value."""

    def __init__(self, value: int, k: int):
        self.value, self.k = value, k
        self.stream_len, self.last_missed_idx = 0, -1

    def add_int(self, integer: int):
        self.stream_len += 1
        if integer != self.value:
            self.last_missed_idx += self.stream_len - 1 - self.last_missed_idx
            return False
        return True if self.last_missed_idx < self.stream_len - self.k else False
