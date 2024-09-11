
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class SubtreeSum:  # LeetCode Q.508.
    def __init__(self) -> None:
        self.occurrences_table, self.max_occurrences = dict(), 0

    def find_most_frequent_sum(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        self.occurrences_table.clear()  # Reset before DFS.
        self.max_occurrences -= self.max_occurrences
        self._dfs_subtree_sum(root)
        return [key for key, value in self.occurrences_table.items() if value == self.max_occurrences]

    def _dfs_subtree_sum(self, node: TreeNode) -> int:
        left_subtree_sum = 0
        if node.left:
            left_subtree_sum += self._dfs_subtree_sum(node.left)

        right_subtree_sum = 0
        if node.right:
            right_subtree_sum += self._dfs_subtree_sum(node.right)

        subtree_sum = node.val + left_subtree_sum + right_subtree_sum
        if subtree_sum not in self.occurrences_table.keys():
            self.occurrences_table.update({subtree_sum: 0})

        self.occurrences_table[subtree_sum] += 1
        if self.occurrences_table[subtree_sum] > self.max_occurrences:
            self.max_occurrences += 1
        return subtree_sum
