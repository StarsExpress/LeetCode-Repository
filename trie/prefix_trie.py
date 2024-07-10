
total_letters = 26  # 26 lower cases.


class TrieNode:
    def __init__(self):
        self.child_node = [None] * total_letters  # Child nodes of each node.
        self.word_end = False  # If any word stops at this node.


class PrefixTrie:  # LeetCode Q.208.
    """Word & prefix insertion & search."""

    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word: str):
        current_node = self.root
        for char in word:
            # Iterated char hasn't had a node in trie.
            if not current_node.child_node[ord(char) - ord("a")]:
                # Open a new node for this char.
                current_node.child_node[ord(char) - ord("a")] = TrieNode()

            # Move to iterated char's node.
            current_node = current_node.child_node[ord(char) - ord("a")]

        current_node.word_end = True  # Last iterated node has a word ending here.

    def search_word(self, word: str):
        current_node = self.root
        for char in word:
            # Iterated char hasn't had a node in trie.
            if not current_node.child_node[ord(char) - ord("a")]:
                return False  # Trie doesn't contain target word.

            current_node = current_node.child_node[ord(char) - ord("a")]

        return current_node.word_end

    def starts_with(self, prefix: str):
        current_node = self.root
        for char in prefix:
            # Iterated char hasn't had a node in trie.
            if not current_node.child_node[ord(char) - ord("a")]:
                return False  # Trie doesn't contain target prefix.

            current_node = current_node.child_node[ord(char) - ord("a")]

        return True
