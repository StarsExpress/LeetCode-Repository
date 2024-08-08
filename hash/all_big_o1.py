
class AllBigO1:  # LeetCode Q.432.
    def __init__(self):
        self.keys_counts = dict()
        self.keys_pool, self.counts_pool = set(), []

    def increment(self, key: str):
        if key not in self.keys_pool:
            self.keys_pool.add(key)
            self.keys_counts.update({key: 0})

        else:  # Remove old count.
            old_count_idx = self._binary_search(self.keys_counts[key])
            self.counts_pool.pop(old_count_idx)

        self.keys_counts[key] += 1  # This is new count.
        new_count_idx = self._binary_search(self.keys_counts[key])
        self.counts_pool.insert(new_count_idx, self.keys_counts[key])

    def decrement(self, key: str):
        if key not in self.keys_pool:
            return

        old_count_idx = self._binary_search(self.keys_counts[key])
        self.counts_pool.pop(old_count_idx)  # Remove old count.

        self.keys_counts[key] -= 1  # This is new count.
        if self.keys_counts[key] == 0:  # 0 count: remove from data structure.
            self.keys_pool.remove(key)
            return

        new_count_idx = self._binary_search(self.keys_counts[key])
        self.counts_pool.insert(new_count_idx, self.keys_counts[key])

    def get_max_key(self):
        for key in self.keys_pool:
            if self.keys_counts[key] == self.counts_pool[-1]:
                return key  # Answer found.
        return ""  # If no key has max count.

    def get_min_key(self):
        for key in self.keys_pool:
            if self.keys_counts[key] == self.counts_pool[0]:
                return key  # Answer found.
        return ""  # If no key has min count.

    def _binary_search(self, count: int):
        if not self.counts_pool:
            return 0

        back_idx, front_idx = 0, len(self.counts_pool) - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.counts_pool[mid_idx] < count:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of counts < target count.
