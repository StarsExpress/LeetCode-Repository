
class MKAverage:  # LeetCode Q.1825.

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.numbers, self.sorted_numbers = [], []

    @staticmethod
    def binary_insert(target: int, sorted_integers: list[int] | tuple[int]):
        if len(sorted_integers) <= 0:
            return 0

        back_idx, front_idx = 0, len(sorted_integers) - 1
        while True:
            if back_idx > front_idx:
                return back_idx  # Number of ints < targets.

            mid_idx = (back_idx + front_idx) // 2
            if sorted_integers[mid_idx] < target:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

    def add_int(self, integer: int):
        while len(self.numbers) >= self.m:
            pop_idx = self.binary_insert(self.numbers[0], self.sorted_numbers)
            self.sorted_numbers.pop(pop_idx)
            self.numbers.pop(0)

        self.numbers.append(integer)
        insertion_idx = self.binary_insert(integer, self.sorted_numbers)
        self.sorted_numbers.insert(insertion_idx, integer)

    def calculate_avg(self):
        if len(self.numbers) < self.m:
            return -1
        return sum(self.sorted_numbers[self.k:-self.k]) // (len(self.numbers) - 2 * self.k)
