
class NestListFlattener:  # LeetCode`Q.341.
    def __init__(self, nested_list):
        self.integers = []
        self._decompose_nested_list(nested_list)

    def _decompose_nested_list(self, nested_list):
        while nested_list:  # Nested list consists of nested int.
            self._dfs_nested_int(nested_list.pop(0))

    def _dfs_nested_int(self, nested_int):
        if nested_int.isInteger():  # Nested int contains a single integer.
            self.integers.append(nested_int.getInteger())
            return

        nested_list = nested_int.getList()
        if not nested_list:
            return
        self._decompose_nested_list(nested_list)  # Nested int contains a nested list.

    def pop_next_int(self):
        return self.integers.pop(0)

    def has_next_int(self):
        return True if self.integers else False
