
class RadixSort:
    """Apply radix sort to sort integers."""

    def __init__(self, integers: list[int] | tuple[int]):
        self.integers = integers

    def radix_sort(self, base_digit: int):
        int_count = len(self.integers)
        sorted_array, quotients = [0] * int_count, [0] * 10

        for i in range(0, int_count):  # Store count of occurrences.
            quotients[(self.integers[i] // base_digit) % 10] += 1

        for i in range(1, 10):  # Change each count to contain base digit's actual position in sorted integers.
            quotients[i] += quotients[i - 1]

        current_idx = -1  # Sort from smallest to biggest: iterate from last to first int.
        while current_idx >= -int_count:
            quotient = self.integers[current_idx] // base_digit
            sorted_array[quotients[quotient % 10] - 1] = self.integers[current_idx]
            quotients[quotient % 10] -= 1
            current_idx -= 1

        self.integers.clear()
        self.integers += sorted_array

    def sort(self):
        maximum, base_digit = max(self.integers), 1  # Base starts from single digit.
        while maximum / base_digit >= 1:
            self.radix_sort(base_digit)
            base_digit *= 10
        return self.integers
