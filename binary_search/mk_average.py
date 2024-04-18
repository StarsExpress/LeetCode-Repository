
class MKAverage:
    """Compute average of last m integers exclusive of k smallest & biggest."""

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.integers, self.sorted_integers = [], []

    def binary_search(self, target: int):
        if len(self.sorted_integers) <= 0:
            return 0

        back_idx, front_idx = 0, len(self.sorted_integers) - 1
        while True:
            if back_idx > front_idx:
                return back_idx  # Number of ints < targets.

            mid_idx = (back_idx + front_idx) // 2
            if self.sorted_integers[mid_idx] < target:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

    def add_integer(self, integer: int) -> None:
        while len(self.integers) >= self.m:
            pop_idx = self.binary_search(self.integers[0])
            self.sorted_integers.pop(pop_idx)
            self.integers.pop(0)

        self.integers.append(integer)
        insertion_idx = self.binary_search(integer)
        self.sorted_integers.insert(insertion_idx, integer)

    def calculate_avg(self) -> int:
        if len(self.integers) < self.m:
            return -1
        return sum(self.sorted_integers[self.k:-self.k]) // (len(self.integers) - 2 * self.k)
