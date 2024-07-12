
total_letters = 26  # 26 lower cases.
min_letter = "a"


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class PrefixTrie:  # LeetCode Q.208.
    """Word & prefix insertion & search."""

    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word: str):
        current_node = self.root
        for char in word:
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                current_node.child_node[idx] = TrieNode()

            current_node = current_node.child_node[idx]

        current_node.word_end = True  # Last iterated node has a word ending here.

    def search_word(self, word: str):
        current_node = self.root
        for char in word:
            idx = ord(char) - ord(min_letter)
            # Iterated char hasn't had a node in trie.
            if not current_node.child_node[idx]:
                return False  # Trie doesn't contain target word.

            current_node = current_node.child_node[idx]

        return current_node.word_end

    def starts_with(self, prefix: str):
        current_node = self.root
        for char in prefix:
            idx = ord(char) - ord(min_letter)
            # Iterated char hasn't had a node in trie.
            if not current_node.child_node[idx]:
                return False  # Trie doesn't contain target prefix.

            current_node = current_node.child_node[idx]

        return True
