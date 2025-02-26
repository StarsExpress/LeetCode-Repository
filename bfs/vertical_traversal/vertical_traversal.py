
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def find_vertical_traversal(root: TreeNode | None) -> list[list[int]]:  # LeetCode Q.987.
    queue = []  # Format: (node, col).
    if root is not None:
        queue.append((root, 0))

    cols2nums: dict[int, list[int]] = dict()
    next_level_nodes = []  # Format: (node, col).
    current_row_values: dict[int, list[int]] = dict()  # Keys: cols.

    while queue:
        node, col = queue.pop(0)
        if node.left:
            next_level_nodes.append((node.left, col - 1))
        if node.right:
            next_level_nodes.append((node.right, col + 1))

        if col not in cols2nums.keys():
            cols2nums[col] = []

        if col not in current_row_values.keys():
            current_row_values[col] = []
        current_row_values[col].append(node.val)
        current_row_values[col].sort()

        if not queue:  # Current level BFS is done.
            queue.extend(next_level_nodes)  # Put next level into queue.
            next_level_nodes.clear()

            for col, values in current_row_values.items():
                cols2nums[col].extend(values)
            current_row_values.clear()

    cols2nums = dict(sorted(cols2nums.items()))
    vertical_traversal = []
    for col, nums in cols2nums.items():
        vertical_traversal.append(nums)
    return vertical_traversal
