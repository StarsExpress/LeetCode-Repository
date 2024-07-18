
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeCompleteness:  # LeetCode Q.958.
    def __init__(self):
        pass

    def check_completeness(self, root: TreeNode | None):
        if root is None:
            return False

        return self._bfs_completeness(root)

    @staticmethod
    def _bfs_completeness(root: TreeNode | None):
        if not root.left and not root.right:  # Only root node.
            return True

        # Format: parent node's idx at parent's level, left child, right child.
        queue = [(0, root.left, root.right)]
        next_level_nodes = []

        current_level_idx = 1  # Root is at level 0. BFS starts from level 1.
        # Indices of leftmost & rightmost children at current level.
        left_end_idx, right_end_idx = None, None
        children_count = 0

        while queue:
            parent_idx, left_node, right_node = queue.pop(0)
            child_nodes = [left_node, right_node]

            for i in range(2):
                if child_nodes[i]:
                    children_count += 1

                    child_idx = parent_idx * 2
                    if i == 1:  # Right child idx needs to add 1.
                        child_idx += 1

                    if left_end_idx is None:
                        left_end_idx = child_idx

                    else:  # Once left end is set, not None child updates right end.
                        right_end_idx = child_idx

                    if child_nodes[i].left or child_nodes[i].right:
                        next_level_nodes.append(
                            (child_idx, child_nodes[i].left, child_nodes[i].right)
                        )

            if not queue:  # Current level BFS is done. Detect incompleteness.
                # Left end ix won't be None, implying child(ren) existence.
                if left_end_idx != 0:  # Leftmost child doesn't sit at left end.
                    return False

                if right_end_idx is None:  # Only one child: treat right end idx as 0.
                    right_end_idx = 0
                if 1 + right_end_idx - left_end_idx != children_count:
                    return False  # A middle child doesn't sit as far left as possible.

                if children_count < 2 ** current_level_idx:  # Current level not full.
                    if next_level_nodes:  # Next level has nodes.
                        return False  # Another incompleteness.

                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()

                current_level_idx += 1  # Update for next level BFS.
                left_end_idx, right_end_idx = None, None  # Reset for next level BFS.
                children_count -= children_count

        return True  # All BFS passed. Binary tree is complete.
