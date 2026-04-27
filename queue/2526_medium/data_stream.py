
class DataStream:  # LeetCode Q.2526.
    """Check if last k integers all equal certain value."""
    def __init__(self, value: int, k: int) -> None:
        self.value, self.k = value, k
        self.stream_len, self.last_missed_idx = 0, -1

    def add_int(self, integer: int) -> bool:
        self.stream_len += 1
        if integer != self.value:
            self.last_missed_idx = self.stream_len - 1
            return False
        return self.last_missed_idx < self.stream_len - self.k
