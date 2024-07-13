
total_letters = 26  # 26 lower cases.
min_letter = "a"


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class SumMapper:  # LeetCode Q.677.
    """Sum all values of words that start with a given prefix."""

    def __init__(self):
        self.root = TrieNode()
        self.values_dict = dict()
        self.values_sum = 0

    def insert(self, word: str, val: int):
        if word not in self.values_dict.keys():  # New word must climb trie before updating dict.
            current_node = self.root
            for char in word:
                idx = ord(char) - ord(min_letter)
                if not current_node.child_node[idx]:
                    current_node.child_node[idx] = TrieNode()

                current_node = current_node.child_node[idx]

            current_node.word_end = True  # Last iterated node has a word ending here.

        self.values_dict.update({word: val})

    def _search_last_node(self, word: str):
        """Given a word, find out its last stopping node in trie."""
        current_node = self.root
        for char in word:
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                return None  # Return None if word isn't among trie.

            current_node = current_node.child_node[idx]

        return current_node

    def _dfs_descendants_values(self, starting_node: TrieNode, word_prefix: str):
        """
        Given a starting node and its word prefix, sum descendants' values.
        """
        if starting_node.word_end:
            self.values_sum += self.values_dict[word_prefix]

        for i in range(total_letters):  # Recursively visit each child node in lex order.
            if starting_node.child_node[i]:
                self._dfs_descendants_values(
                    starting_node.child_node[i], word_prefix + chr(i + ord(min_letter))
                )

    def sum(self, prefix: str):
        self.values_sum = 0  # Reset once sum method is called.

        last_node = self._search_last_node(prefix)
        if last_node:  # Potential matches exist.
            self._dfs_descendants_values(last_node, prefix)
        return self.values_sum
