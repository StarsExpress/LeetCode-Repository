
class MedianFinder:  # LeetCode Q.295.
    """Find median stream."""

    def __init__(self):
        self.nums, self.min_root, self.max_root = {'min': [], 'max': []}, float('inf'), float('-inf')

    def insert_heap(self, num, heap: str):
        self.nums[heap].append(num)
        if heap == 'min':
            if num < self.min_root:
                self.min_root = num
            return
        if num > self.max_root:
            self.max_root = num

    def remove_root(self, heap: str):
        if heap == 'min':
            self.nums[heap].remove(self.min_root)
            self.min_root = min(self.nums[heap]) if len(self.nums[heap]) > 0 else float('inf')
            return
        self.nums[heap].remove(self.max_root)
        self.max_root = max(self.nums[heap]) if len(self.nums[heap]) > 0 else float('-inf')

    def add_num(self, num: int):
        if len(self.nums['min']) + len(self.nums['max']) <= 0:
            self.insert_heap(num, 'min')
            return

        if len(self.nums['max']) == len(self.nums['min']):
            if self.max_root <= num <= self.min_root:
                self.insert_heap(num, 'max')
                return
            if num <= self.max_root <= self.min_root:
                self.insert_heap(self.max_root, 'min')
                self.remove_root('max')
                self.insert_heap(num, 'max')
                return
            self.insert_heap(self.min_root, 'max')
            self.remove_root('min')
            self.insert_heap(num, 'min')
            return

        if len(self.nums['max']) > len(self.nums['min']):
            if num < self.max_root:
                self.insert_heap(self.max_root, 'min')
                self.remove_root('max')
                self.insert_heap(num, 'max')
                return
            self.insert_heap(num, 'min')
            return

        if len(self.nums['min']) > len(self.nums['max']):
            if num > self.min_root:
                self.insert_heap(self.min_root, 'max')
                self.remove_root('min')
                self.insert_heap(num, 'min')
                return
            self.insert_heap(num, 'max')

    def find_median(self):
        if len(self.nums['min']) == len(self.nums['max']):
            return (self.min_root + self.max_root) / 2

        if len(self.nums['min']) < len(self.nums['max']):
            return self.max_root

        if len(self.nums['min']) > len(self.nums['max']):
            return self.min_root
