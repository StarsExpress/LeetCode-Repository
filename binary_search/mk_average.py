
class MKAverage:  # LeetCode Q.1825.
    """Compute average of last m integers exclusive of k smallest & biggest."""

    def __init__(self, m: int, k: int) -> None:
        self.m, self.k = m, k
        self.integers, self.sorted_integers = [], []
        self.total_numbers = 0

    def _binary_search(self, target: int) -> int:
        left_idx, right_idx = 0, self.total_numbers - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if self.sorted_integers[mid_idx] < target:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        return left_idx  # Number of ints < target.

    def add_integer(self, integer: int) -> None:
        while self.total_numbers >= self.m:
            pop_idx = self._binary_search(self.integers[0])
            self.sorted_integers.pop(pop_idx)
            self.integers.pop(0)
            self.total_numbers -= 1

        self.integers.append(integer)
        insertion_idx = self._binary_search(integer)
        self.sorted_integers.insert(insertion_idx, integer)
        self.total_numbers += 1

    def calculate_avg(self) -> int:
        if self.total_numbers < self.m:
            return -1
        return sum(self.sorted_integers[self.k: -self.k]) // (self.total_numbers - 2 * self.k)
