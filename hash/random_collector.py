from random import randrange


class RandomCollector:  # LeetCode Q.381.
    def __init__(self):
        self.counts_table = dict()
        self.values_pool, self.pool_size = [], 0

    def insert(self, value: int):
        if value not in self.counts_table.keys():
            self.counts_table.update({value: 0})
        self.counts_table[value] += 1

        self.values_pool.append(value)
        self.pool_size += 1
        return self.counts_table[value] == 1

    def remove(self, value: int):
        if value not in self.counts_table.keys():
            return False
        if self.counts_table[value] == 0:
            return False

        self.counts_table[value] -= 1
        self.values_pool.remove(value)
        self.pool_size -= 1
        return True

    def get_random_value(self):
        return self.values_pool[randrange(self.pool_size)]
