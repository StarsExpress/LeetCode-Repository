
total_digits = 10
min_digit = "0"


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_digits
        self.integer_end = False  # If any integer stops at this node.


class IntegerTrie:  # LeetCode Q.386.
    """Integer insertion & lex sorting."""
    def __init__(self):
        self.root = TrieNode()

    def insert_int(self, integer: int):
        current_node, integer = self.root, str(integer)
        for digit in integer:
            idx = ord(digit) - ord(min_digit)
            if not current_node.child_node[idx]:
                current_node.child_node[idx] = TrieNode()

            current_node = current_node.child_node[idx]

        current_node.integer_end = True  # Last iterated node has an int ending here.

    def _dfs_descendants(
        self, starting_node: TrieNode, digit_prefix: str, sorted_ints: list[int]
    ):
        """
        Given a starting node and its digit prefix, find descendants in lex order.
        """
        if starting_node.integer_end:  # Node is end of an int, which is int(prefix).
            sorted_ints.append(int(digit_prefix))

        for i in range(total_digits):  # Recursively visit each child node in lex order.
            if starting_node.child_node[i]:
                self._dfs_descendants(
                    starting_node.child_node[i],
                    digit_prefix + chr(i + ord(min_digit)),
                    sorted_ints
                )

    def sort_lex_order(self):
        sorted_ints = []
        self._dfs_descendants(self.root, "", sorted_ints)
        return sorted_ints
