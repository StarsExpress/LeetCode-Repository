
class FrequencyStack:  # LeetCode Q.895.
    def __init__(self):
        self.values_freqs = dict()
        self.values_pool, self.freqs_pool = [], []

    def push(self, value: int):
        self.values_pool.append(value)

        if value not in self.values_freqs:
            self.values_freqs.update({value: 0})

        else:  # Remove old freq.
            old_freq_idx = self._binary_search(self.values_freqs[value])
            self.freqs_pool.pop(old_freq_idx)

        self.values_freqs[value] += 1  # This is new freq.
        new_freq_idx = self._binary_search(self.values_freqs[value])
        self.freqs_pool.insert(new_freq_idx, self.values_freqs[value])

    def pop(self):
        """
        Find the value with the highest frequency. If there is a tie,
        remove and return the value closest to stack's top.
        """
        pool_idx = -1
        while pool_idx >= -len(self.values_pool):
            if self.values_freqs[self.values_pool[pool_idx]] == self.freqs_pool[-1]:
                self.freqs_pool.pop(-1)  # Remove old freq.

                self.values_freqs[self.values_pool[pool_idx]] -= 1
                new_freq = self.values_freqs[self.values_pool[pool_idx]]
                new_freq_idx = self._binary_search(new_freq)
                self.freqs_pool.insert(new_freq_idx, new_freq)
                return self.values_pool.pop(pool_idx)

            pool_idx -= 1

    def _binary_search(self, frequency: int):
        if not self.freqs_pool:
            return 0

        back_idx, front_idx = 0, len(self.freqs_pool) - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.freqs_pool[mid_idx] < frequency:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of frequencies < target frequency.
