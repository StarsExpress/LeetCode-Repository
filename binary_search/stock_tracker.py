
class StockPriceTracker:  # LeetCode Q.2034.
    """Track stock prices fluctuations."""

    def __init__(self) -> None:
        # Records: timestamps are keys and prices are values.
        self.records, self.latest_time = dict(), -1
        # Prices are sorted from smallest to biggest.
        self.prices, self.prices_count = [], 0

    def _binary_search(self, target: int) -> int:
        left_idx, right_idx = 0, self.prices_count - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if self.prices[mid_idx] < target:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        return left_idx  # Number of ints < target.

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.latest_time:
            self.latest_time += timestamp - self.latest_time

        if timestamp in self.records.keys():
            pop_idx = self._binary_search(self.records[timestamp])
            self.prices.pop(pop_idx)
            self.prices_count -= 1

        self.records.update({timestamp: price})
        insertion_idx = self._binary_search(price)
        self.prices.insert(insertion_idx, price)
        self.prices_count += 1

    def current(self) -> int:
        return self.records[self.latest_time]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]
