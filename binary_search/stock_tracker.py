
class StockPriceTracker:  # LeetCode Q.2034.
    """Track stock prices fluctuations."""

    def __init__(self):
        # Records: timestamps as keys and prices as values.
        # Prices list is sorted from smallest to biggest.
        self.records, self.prices, self.latest_time = dict(), [], -1

    def binary_search(self, target: int):
        if not self.prices:
            return 0

        back_idx, front_idx = 0, len(self.prices) - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.prices[mid_idx] < target:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of ints < target.

    def update(self, timestamp: int, price: int):
        if timestamp in self.records.keys():
            pop_idx = self.binary_search(self.records[timestamp])
            self.prices.pop(pop_idx)
        self.records.update({timestamp: price})

        if timestamp > self.latest_time:
            self.latest_time += timestamp - self.latest_time

        insertion_idx = self.binary_search(price)
        self.prices.insert(insertion_idx, price)

    def current(self):
        return self.records[self.latest_time]

    def maximum(self):
        return self.prices[-1]

    def minimum(self):
        return self.prices[0]
