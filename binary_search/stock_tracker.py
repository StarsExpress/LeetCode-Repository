class StockPrice:

    def __init__(self):
        # Records: timestamps are keys and prices are values.
        # Prices list is sorted from smallest to biggest.
        self.records, self.prices, self.latest_time = dict(), [], -1

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

    def update(self, timestamp: int, price: int):
        if timestamp in self.records.keys():
            self.prices.remove(self.records[timestamp])
        self.records.update({timestamp: price})

        if timestamp > self.latest_time:
            self.latest_time += timestamp - self.latest_time

        insertion_idx = self.binary_insert(price, self.prices)
        self.prices.insert(insertion_idx, price)

    def current(self):
        return self.records[self.latest_time]

    def maximum(self):
        return self.prices[-1]

    def minimum(self):
        return self.prices[0]
