
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class TreeRecovery:  # LeetCode Q.1028.
    def __init__(self) -> None:
        self.nodes_and_levels = []

    def recover(self, traversal: str) -> TreeNode | None:
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

    def _dfs_recover_tree(self, node: TreeNode, current_level: int) -> int:
        node_dashes = 0
        while self.nodes_and_levels and self.nodes_and_levels[0] == "-":
            self.nodes_and_levels.pop(0)
            node_dashes += 1

        if node_dashes != current_level + 1:  # Current node is leaf node.
            return node_dashes  # End current route DFS.

        left_node_value = ""
        while self.nodes_and_levels and self.nodes_and_levels[0].isdigit():
            left_node_value += self.nodes_and_levels.pop(0)

        node.left = TreeNode(int(left_node_value))
        left_child_dashes = self._dfs_recover_tree(node.left, current_level + 1)

        if left_child_dashes != current_level + 1:  # Left side reaches leaf node.
            return left_child_dashes  # End current route DFS.

        right_node_value = ""
        while self.nodes_and_levels and self.nodes_and_levels[0].isdigit():
            right_node_value += self.nodes_and_levels.pop(0)

        node.right = TreeNode(int(right_node_value))
        # Right side reaches leaf node. End current route DFS.
        return self._dfs_recover_tree(node.right, current_level + 1)
