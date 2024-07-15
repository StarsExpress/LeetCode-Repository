
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RowAddition:  # LeetCode Q.623.
    def __init__(self):
        self.val, self.depth = None, None

    def add_row(self, root: TreeNode | None, val: int, depth: int):
        if root is None:
            return root

        if depth == 1:  # Addition at root.
            return TreeNode(val=val, left=root)

        self.val, self.depth = val, depth
        self._dfs_descendants_nodes(None, root, 0)
        return root

    def _dfs_descendants_nodes(
        self, parent_node: TreeNode | None, current_node: TreeNode, path_edges: int
    ):
        """
        Path edges = edges count from root to current node. Plus 1 gets current node level.
        When a node is added, its "original" attribute is marked as False.
        This prevents excessive node addition in DFS.
        """
        path_edges += 1
        if "original" not in current_node.__dict__.keys():
            current_node.original = True  # Default to True.

        # Current node is an original node by program.
        if current_node.original and path_edges == self.depth:
            if parent_node.left == current_node:  # Left child.
                parent_node.left = TreeNode(val=self.val, left=current_node)

                if not parent_node.right:  # Help parent add right child if not exists.
                    parent_node.right = TreeNode(val=self.val)
                    parent_node.right.original = False  # Added node isn't original.

            if parent_node.right == current_node:  # Right child.
                parent_node.right = TreeNode(val=self.val, right=current_node)

                if not parent_node.left:  # Help parent add left child if not exists.
                    parent_node.left = TreeNode(val=self.val)
                    parent_node.left.original = False  # Added node isn't original.

            return  # Addition done. End DFS.

        if current_node.left:
            self._dfs_descendants_nodes(current_node, current_node.left, path_edges)

        if current_node.right:
            self._dfs_descendants_nodes(current_node, current_node.right, path_edges)

        if not current_node.left and not current_node.right:
            if path_edges + 1 == self.depth:  # Addition at leaf nodes.
                current_node.left = TreeNode(val=self.val)
                current_node.right = TreeNode(val=self.val)
