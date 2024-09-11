
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class UniValuePath:  # LeetCode Q.687.
    def __init__(self) -> None:
        self.max_len = 0

    def find_longest_path(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        self.max_len -= self.max_len  # Reset to 0 before DFS.
        self._dfs_count_uni_length(root)
        return self.max_len

    def _dfs_count_uni_length(self, node: TreeNode, parent_value: int = None) -> int:
        """
        For a node, number of consecutive descendants of same value is the longest
        univalue path length from this node to descendants of same value.
        """
        parent_same = True if node.val == parent_value else False

        left_uni_len = 0  # Consecutive left descendants of same value as current node.
        if node.left:
            left_uni_len += self._dfs_count_uni_length(node.left, node.val)

        right_uni_len = 0  # Consecutive right descendants of same value as current node.
        if node.right:
            right_uni_len += self._dfs_count_uni_length(node.right, node.val)

        if left_uni_len + right_uni_len > self.max_len:  # Max len can occur as a "semi-cycle".
            self.max_len = left_uni_len + right_uni_len

        if parent_same:  # 1 indicates the edge between parent and current node.
            return max(1 + left_uni_len, 1 + right_uni_len)

        if max(left_uni_len, right_uni_len) > self.max_len:
            self.max_len = max(left_uni_len, right_uni_len)
        return 0  # 0 consecutive descendants of same value as parent node.
