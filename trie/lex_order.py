
total_digits = 10


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
            # Iterated digit hasn't had a node in trie.
            if not current_node.child_node[ord(digit) - ord("0")]:
                # Open a new node for this digit.
                current_node.child_node[ord(digit) - ord("0")] = TrieNode()

            # Move to iterated digit's node.
            current_node = current_node.child_node[ord(digit) - ord("0")]

        current_node.integer_end = True  # Last iterated node has an int ending here.

    def _dfs_int(
        self, current_node: TrieNode, digit_prefix: str, sorted_ints: list[int]
    ):
        if current_node.integer_end:  # Current node is end of an int: prefix can join sorted list.
            sorted_ints.append(int(digit_prefix))

        for i in range(total_digits):  # Recursively visit each child node in lex order.
            if current_node.child_node[i] is not None:
                self._dfs_int(current_node.child_node[i], digit_prefix + chr(i + ord("0")), sorted_ints)

    def sort_lex_order(self):
        sorted_ints = []
        self._dfs_int(self.root, "", sorted_ints)
        return sorted_ints
