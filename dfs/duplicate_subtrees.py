
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DuplicateSubtrees:  # LeetCode Q.652.
    def __init__(self):
        self.subtrees = None

    def find_duplicate_subtrees(self, root: TreeNode | None):
        if root is None:
            return []

        self.subtrees = []
        self._dfs_subtree(root)

        occurred_values = set()
        duplicate_values, duplicate_nodes = set(), []
        while self.subtrees:
            subtree_values, subtree_nodes = self.subtrees.pop()
            if subtree_values not in occurred_values:
                occurred_values.add(subtree_values)
                continue

            if subtree_values not in duplicate_values:
                duplicate_values.add(subtree_values)
                duplicate_nodes.append(subtree_nodes)
                continue

        return duplicate_nodes

    def _dfs_subtree(self, current_node: TreeNode):
        """Subtrees' values are stored in string as hash mark."""
        if current_node.left:
            left_subtree_values = self._dfs_subtree(current_node.left)

        else:
            left_subtree_values = "None-"  # Non-existent left child: slash at right.

        if current_node.right:
            right_subtree_values = self._dfs_subtree(current_node.right)

        else:
            right_subtree_values = "-None"  # Non-existent right child: slash at left.

        subtree_values = left_subtree_values + str(current_node.val) + right_subtree_values
        self.subtrees.append((subtree_values, current_node))
        return subtree_values
