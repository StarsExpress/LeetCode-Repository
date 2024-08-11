
class LFUCache:  # LeetCode Q.460.
    """Least Frequently Used (LFU) Cache."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys_values, self.keys_usages = dict(), dict()
        self.keys_pool, self.usages_pool = [], []

    def get(self, key: int):
        try:
            self.keys_values[key]

        except KeyError:
            return -1

        self.keys_pool.remove(key)
        old_usage_idx = self._binary_search(self.keys_usages[key]) - 1
        self.usages_pool.pop(old_usage_idx)

        self.keys_usages[key] += 1
        new_usage_idx = self._binary_search(self.keys_usages[key])

        self.keys_pool.insert(new_usage_idx, key)
        self.usages_pool.insert(new_usage_idx, self.keys_usages[key])

        return self.keys_values[key]

    def put(self, key: int, value: int):
        try:
            self.keys_values[key]

        except KeyError:
            if self.capacity == 0:
                self.usages_pool.pop(0)

                deleted_key = self.keys_pool.pop(0)
                del self.keys_values[deleted_key]
                del self.keys_usages[deleted_key]

                self.capacity += 1

            self.keys_values.update({key: value})
            self.keys_usages.update({key: 1})

            usage_idx = self._binary_search(1)
            self.keys_pool.insert(usage_idx, key)
            self.usages_pool.insert(usage_idx, 1)

            self.capacity -= 1
            return

        self.keys_values.update({key: value})

        self.keys_pool.remove(key)
        old_usage_idx = self._binary_search(self.keys_usages[key]) - 1
        self.usages_pool.pop(old_usage_idx)

        self.keys_usages[key] += 1
        new_usage_idx = self._binary_search(self.keys_usages[key])

        self.keys_pool.insert(new_usage_idx, key)
        self.usages_pool.insert(new_usage_idx, self.keys_usages[key])

    def _binary_search(self, usage: int):
        if not self.usages_pool:
            return 0

        back_idx, front_idx = 0, len(self.usages_pool) - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.usages_pool[mid_idx] <= usage:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of usages <= target usage.
