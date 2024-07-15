
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class UniqueValuePath:  # LeetCode Q.687.
    def __init__(self):
        self.max_len = 0

    def find_longest_path(self, root: TreeNode | None):
        if root is None:
            return 0
        self.max_len -= self.max_len  # Reset to 0 before DFS.
        self._dfs_descendants_edges(root)
        return self.max_len

    def _dfs_descendants_edges(self, current_node: TreeNode, parent_node_value: int = None):
        """
        For a node, number of consecutive descendants of same value is the longest
        univalue path length from this node to descendants of same value.
        """
        parent_same = True if current_node.val == parent_node_value else False

        left_edges = 0  # Number of consecutive left descendants of same value as current node.
        if current_node.left:
            left_edges += self._dfs_descendants_edges(current_node.left, current_node.val)

        right_edges = 0  # Number of consecutive right descendants of same value as current node.
        if current_node.right:
            right_edges += self._dfs_descendants_edges(current_node.right, current_node.val)

        if left_edges + right_edges > self.max_len:  # Max len can occur as a "semi-cycle".
            self.max_len = left_edges + right_edges

        if parent_same:  # 1 indicates the edge between parent and current node.
            return max(1 + left_edges, 1 + right_edges)

        if max(left_edges, right_edges) > self.max_len:
            self.max_len = max(left_edges, right_edges)
        return 0  # 0 consecutive descendants of same value as parent node.
