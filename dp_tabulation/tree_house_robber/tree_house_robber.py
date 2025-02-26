
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeHouseRobber:  # LeetCode Q.337.
    def __init__(self):
        self.max_robbery = 0

    def rob_max_properties(self, root: TreeNode | None):
        self.max_robbery -= self.max_robbery  # Reset before DFS.
        self._dfs_money(root)
        return self.max_robbery

    def _dfs_money(self, current_node: TreeNode | None):
        if current_node is None:  # Non-existent node.
            return 0, 0  # MIS two before set cum value & last set cum value.

        # Track two before & last sets' cum values in both sides.
        left_two_before, left_last = self._dfs_money(current_node.left)
        right_two_before, right_last = self._dfs_money(current_node.right)

        total_two_before = left_two_before + right_two_before  # Merge both sides.
        total_last = left_last + right_last

        if total_two_before + current_node.val > total_last:  # Two before set wins.
            total_last = max(total_two_before, total_last)
            total_two_before += current_node.val
            # Swap two sets before returning to parent node.
            total_two_before, total_last = total_last, total_two_before

        else:  # Last set wins.
            total_two_before = total_last

        max_robbery = max(total_two_before, total_last)
        if max_robbery > self.max_robbery:
            self.max_robbery = max_robbery

        return total_two_before, total_last
