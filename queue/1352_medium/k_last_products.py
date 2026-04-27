
class KLastProducts:  # LeetCode Q.1352.
    """Calculate product of last k integers."""
    def __init__(self) -> None:
        self.non_zero_prefix_products, self.products_count = [], 0

    def add_int(self, integer: int) -> None:
        if integer == 0:  # Reset prefix products.
            self.non_zero_prefix_products.clear()
            self.products_count -= self.products_count
            return

        if self.products_count == 0:
            self.non_zero_prefix_products.append(integer)

        else:
            self.non_zero_prefix_products.append(
                self.non_zero_prefix_products[-1] * integer
            )

        self.products_count += 1

    def find_product(self, k: int) -> int:
        if k > self.products_count:  # Last k ints have 0.
            return 0

        if self.products_count == k:  # Exactly last k consecutive non-zero ints.
            return self.non_zero_prefix_products[-1]  # Take the last prefix product.
        return self.non_zero_prefix_products[-1] // self.non_zero_prefix_products[-1 - k]
