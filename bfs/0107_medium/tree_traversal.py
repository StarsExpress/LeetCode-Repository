
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def travel_nodes(root: TreeNode | None) -> list[list[int]]:  # LeetCode Q.102 & 107.
    traveled_nodes = []

    if root is not None:
        queue = [root]
        current_level_nodes, next_level_nodes = [], []
        while queue:
            node = queue.pop(0)
            if node:
                current_level_nodes.append(node.val)

                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            if not queue:  # Current level BFS is done.
                # Use copy to ensure final output is list[list[int]].
                traveled_nodes.append(current_level_nodes.copy())
                current_level_nodes.clear()

                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()

    return traveled_nodes[::-1]
