
class MedianFinder:  # LeetCode Q.295.
    """Find median stream."""

    def __init__(self):
        self.numbers, self.min_root, self.max_root = {'min': [], 'max': []}, float('inf'), float('-inf')

    def insert_heap(self, number, heap: str):
        self.numbers[heap].append(number)
        if heap == 'min':
            if number < self.min_root:
                self.min_root = number
            return

        if number > self.max_root:
            self.max_root = number

    def remove_root(self, heap: str):
        if heap == 'min':
            self.numbers[heap].remove(self.min_root)
            self.min_root = min(self.numbers[heap]) if len(self.numbers[heap]) > 0 else float('inf')
            return

        self.numbers[heap].remove(self.max_root)
        self.max_root = max(self.numbers[heap]) if len(self.numbers[heap]) > 0 else float('-inf')

    def add_num(self, num: int):
        if len(self.numbers['min']) + len(self.numbers['max']) <= 0:
            self.insert_heap(num, 'min')
            return

        if len(self.numbers['max']) == len(self.numbers['min']):
            if self.max_root <= num <= self.min_root:
                self.insert_heap(num, 'max')
                return

            if num <= self.max_root:
                self.insert_heap(self.max_root, 'min')
                self.remove_root('max')
                self.insert_heap(num, 'max')
                return

            self.insert_heap(self.min_root, 'max')
            self.remove_root('min')
            self.insert_heap(num, 'min')
            return

        if len(self.numbers['max']) > len(self.numbers['min']):
            if num < self.max_root:
                self.insert_heap(self.max_root, 'min')
                self.remove_root('max')
                self.insert_heap(num, 'max')
                return

            self.insert_heap(num, 'min')
            return

        if len(self.numbers['min']) > len(self.numbers['max']):
            if num > self.min_root:
                self.insert_heap(self.min_root, 'max')
                self.remove_root('min')
                self.insert_heap(num, 'min')
                return

            self.insert_heap(num, 'max')

    def find_median(self):
        if len(self.numbers['min']) == len(self.numbers['max']):
            return (self.min_root + self.max_root) / 2

        if len(self.numbers['min']) < len(self.numbers['max']):
            return self.max_root

        if len(self.numbers['min']) > len(self.numbers['max']):
            return self.min_root
