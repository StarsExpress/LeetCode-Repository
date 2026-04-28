
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def find_level_max(root: TreeNode | None) -> list[int]:  # LeetCode Q.515.
    levels_max = []
    if root is not None:
        levels_max.append(root.val)

        queue = []
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

        if not queue:
            return levels_max

        next_level_nodes = []
        level_max = -float("inf")

        while queue:
            node = queue.pop(0)
            if node.val > level_max:
                level_max = node.val

            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)

            if not queue:  # Current level BFS is done.
                levels_max.append(level_max)

                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()
                level_max = -float("inf")  # Reset for next level BFS.

    return levels_max
