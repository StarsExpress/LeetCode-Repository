
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeRecovery:  # LeetCode Q.1028.
    def __init__(self):
        self.nodes_and_levels = []

    def recoverFromPreorder(self, traversal: str):
        self.nodes_and_levels.clear()  # Reset before recovery.
        self.nodes_and_levels.extend(list(traversal))

        root_value = ""
        while self.nodes_and_levels:
            if self.nodes_and_levels[0] == "-":
                break
            root_value += self.nodes_and_levels.pop(0)

        root = TreeNode(int(root_value))
        self._dfs_recover_tree(root, 0)
        return root

    def _dfs_recover_tree(self, node: TreeNode, current_level: int):
        # Number of dashes before a node: the level this node belongs to.
        num_dashes = 0
        while self.nodes_and_levels:
            if self.nodes_and_levels[0] != "-":
                break
            self.nodes_and_levels.pop(0)
            num_dashes += 1

        if num_dashes != current_level + 1:
            return num_dashes  # DFS reaches end in current route.

        left_child_value = ""
        while self.nodes_and_levels:
            if self.nodes_and_levels[0] == "-":
                break
            left_child_value += self.nodes_and_levels.pop(0)
        left_child_value = int(left_child_value)

        node.left = TreeNode(left_child_value)
        left_child_dashes = self._dfs_recover_tree(node.left, current_level + 1)

        if left_child_dashes != current_level + 1:
            return left_child_dashes  # DFS reaches end in current route.

        right_child_value = ""
        while self.nodes_and_levels:
            if self.nodes_and_levels[0] == "-":
                break
            right_child_value += self.nodes_and_levels.pop(0)
        right_child_value = int(right_child_value)

        node.right = TreeNode(right_child_value)
        right_child_dashes = self._dfs_recover_tree(node.right, current_level + 1)
        return right_child_dashes  # DFS reaches end in current route.
