
class KLastProducts:  # LeetCode Q.1352.
    """Calculate product of last k integers."""
    def __init__(self) -> None:
        self.stream_len, self.non_zero_products, self.last_zero_idx = 0, [], -1

    def add_int(self, integer: int) -> None:
        self.stream_len += 1
        if integer == 1:
            self.non_zero_products.append(integer)
            return

        if integer == 0:
            self.last_zero_idx += self.stream_len - 1 - self.last_zero_idx
            self.non_zero_products.clear()
            return

        for i in range(len(self.non_zero_products)):
            self.non_zero_products[i] *= integer
        self.non_zero_products.append(integer)

    def find_product(self, k: int) -> int:
        if self.last_zero_idx >= self.stream_len - k:  # Last k integers have 0.
            return 0
        return self.non_zero_products[-k]
