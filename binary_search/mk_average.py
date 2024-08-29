
class MKAverage:  # LeetCode Q.1825.
    """Compute average of last m integers exclusive of k smallest & biggest."""
    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.integers, self.sorted_integers = [], []
        self.total_numbers = 0

    def _binary_search(self, target: int):
        if self.total_numbers == 0:
            return 0

        back_idx, front_idx = 0, self.total_numbers - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.sorted_integers[mid_idx] < target:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of ints < target.

    def add_integer(self, integer: int):
        while self.total_numbers >= self.m:
            pop_idx = self._binary_search(self.integers[0])
            self.sorted_integers.pop(pop_idx)
            self.integers.pop(0)
            self.total_numbers -= 1

        self.integers.append(integer)
        insertion_idx = self._binary_search(integer)
        self.sorted_integers.insert(insertion_idx, integer)
        self.total_numbers += 1

    def calculate_avg(self):
        if self.total_numbers < self.m:
            return -1
        return sum(self.sorted_integers[self.k: -self.k]) // (self.total_numbers - 2 * self.k)
