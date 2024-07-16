
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeTraversal:  # LeetCode Q.102 & 107.
    def __init__(self):
        self.traveled_nodes = []

    def travel_nodes(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        self.traveled_nodes.clear()  # Reset before traversal.
        self._bfs_binary_tree(root)
        return self.traveled_nodes[::-1]  # Required level order: bottom to top.

    def _bfs_binary_tree(self, root: TreeNode | None):
        queue = [(root, None)]
        current_level_nodes, next_level_nodes = [], []
        while queue:
            left_node, right_node = queue.pop(0)

            if left_node:
                current_level_nodes.append(left_node.val)
                # For nodes with at least a child, add child(ren) to deck.
                if left_node.left or left_node.right:
                    next_level_nodes.append(
                        (left_node.left, left_node.right)
                    )

            if right_node:
                current_level_nodes.append(right_node.val)
                # For nodes with at least a child, add child(ren) to deck.
                if right_node.left or right_node.right:
                    next_level_nodes.append(
                        (right_node.left, right_node.right)
                    )

            if not queue:  # Current level BFS is done.
                # Use copy to ensure final output is list[list[int]].
                self.traveled_nodes.append(current_level_nodes.copy())
                current_level_nodes.clear()

                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()
