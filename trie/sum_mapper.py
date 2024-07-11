
total_letters = 26  # 26 lower cases.
min_letter = "a"


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class SumMapper:  # LeetCode Q.677.
    """Sum all values of keys that start with a given prefix."""

    def __init__(self):
        self.root = TrieNode()
        self.values_dict = dict()
        self.values_sum = 0

    def insert(self, key: str, val: int):
        if key not in self.values_dict.keys():
            current_node = self.root
            for char in key:
                idx = ord(char) - ord(min_letter)
                # Iterated char hasn't had a node in trie.
                if not current_node.child_node[idx]:
                    # Open a new node for this char.
                    current_node.child_node[idx] = TrieNode()

                # Move to iterated char's node.
                current_node = current_node.child_node[idx]

            current_node.word_end = True  # Last iterated node has a word ending here.

        self.values_dict.update({key: val})

    def _search_last_node(self, key: str):
        current_node = self.root
        for char in key:
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                return None  # Return None if key isn't among trie.

            current_node = current_node.child_node[idx]

        return current_node

    def _dfs_descendants_values(self, starting_node: TrieNode, key_prefix: str):
        if starting_node.word_end:
            self.values_sum += self.values_dict[key_prefix]

        for i in range(total_letters):
            if starting_node.child_node[i] is not None:
                self._dfs_descendants_values(
                    starting_node.child_node[i], key_prefix + chr(i + ord(min_letter))
                )

    def sum(self, prefix: str):
        self.values_sum = 0  # Reset once sum method is called.

        last_node = self._search_last_node(prefix)
        if last_node:  # Potential matches exist.
            self._dfs_descendants_values(last_node, prefix)
        return self.values_sum
