
class KLastProducts:
    """Calculate product of last k integers."""

    def __init__(self):
        self.integers, self.non_zero_products, self.last_zero_idx = [], [], -1

    def add_int(self, integer: int):
        self.integers.append(integer)
        if integer == 1:
            self.non_zero_products.append(integer)
            return

        if integer == 0:
            self.last_zero_idx += len(self.integers) - 1 - self.last_zero_idx
            self.non_zero_products.clear()
            return

        for i in range(len(self.non_zero_products)):
            self.non_zero_products[i] *= integer
        self.non_zero_products.append(integer)

    def find_product(self, k: int):
        if k > len(self.integers):
            raise IndexError('K must <= count of received integers.')
        if self.last_zero_idx >= len(self.integers) - k:  # Last k integers have 0.
            return 0
        return self.non_zero_products[-k]
