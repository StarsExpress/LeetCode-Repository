
class Node:
    def __init__(self, val=0, left=None, right=None, next_node=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next_node


class NodesConnector:  # LeetCode Q.116 & 117.
    """Connect nodes at same level in any binary tree."""
    def __init__(self):
        pass

    def connect_nodes(self, root: Node | None):
        if root is None:
            return root

        self._bfs_binary_tree(root)
        return root

    @staticmethod
    def _bfs_binary_tree(root: Node | None):
        # In queue, nodes of same parent are in same tuple. Format: (left child, right child).
        queue = [(root, None)]  # Current level nodes.
        deck = []  # Next level nodes.
        # Once BFS search finishes current level (empty queue), deck joins queue.

        while queue:
            left_node, right_node = queue.pop(0)

            if left_node:
                if right_node:
                    left_node.next = right_node

                if not right_node and queue:
                    if queue[0][0]:  # Queue's 1st left child.
                        left_node.next = queue[0][0]

                    if not queue[0][0] and queue[0][1]:
                        left_node.next = queue[0][1]  # Queue's 1st right child.

            if right_node and queue:
                if queue[0][0]:  # Queue's 1st left child.
                    right_node.next = queue[0][0]

                if not queue[0][0] and queue[0][1]:
                    right_node.next = queue[0][1]  # Queue's 1st right child.

            # For nodes with at least a child, add child(ren) to deck.
            if left_node:
                if left_node.left or left_node.right:
                    deck.append(
                        (left_node.left, left_node.right)
                    )

            if right_node:
                if right_node.left or right_node.right:
                    deck.append(
                        (right_node.left, right_node.right)
                    )

            if not queue:  # BFS search has cleared current level.
                queue.extend(deck)  # Next level's nodes can join.
                deck.clear()
