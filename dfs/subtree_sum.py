
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SubtreeSum:
    def __init__(self, root: TreeNode | None):
        self.root, self.sums = root, []

    def find_most_frequent_sum(self):
        if self.root is None:
            return []

        self._dfs_subtree_sum(self.root)

        occurrences_table, max_occurrences = dict(), 0
        while self.sums:
            popped_sum = self.sums.pop()
            if popped_sum not in occurrences_table.keys():
                occurrences_table.update({popped_sum: 0})

            occurrences_table[popped_sum] += 1
            if occurrences_table[popped_sum] > max_occurrences:
                max_occurrences += 1

        return [key for key, value in occurrences_table.items() if value == max_occurrences]

    def _dfs_subtree_sum(self, current_node: TreeNode):
        left_subtree_sum = 0
        if current_node.left:
            left_subtree_sum += self._dfs_subtree_sum(current_node.left)

        right_subtree_sum = 0
        if current_node.right:
            right_subtree_sum += self._dfs_subtree_sum(current_node.right)

        # Current subtree: subtree centered at current node.
        current_subtree_sum = current_node.val + left_subtree_sum + right_subtree_sum
        self.sums.append(current_subtree_sum)
        return current_subtree_sum
