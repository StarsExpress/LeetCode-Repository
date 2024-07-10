
total_letters = 26  # 26 lower cases.


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class WordDictionary:  # LeetCode Q.211.
    """Fuzzy word search."""

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
        """
        During word search, return true if any word matches target word or false otherwise.
        Target word may contain dots "." where dots can be matched with any letter.
        """
        return self.search_recursive(self.root, word, 0)
    
    def search_recursive(self, node: TrieNode, word: str, word_idx: int):
        """Encounters word search with dots as a special pass."""
        if word_idx == len(word):  # Check if current node is end of a word.
            return node.word_end

        char = word[word_idx]  # Current character.
        if char == ".":  # Dot: check all possible child nodes.
            for child in node.child_node:
                # Child node exists and recursive call finds matches.
                if child and self.search_recursive(child, word, word_idx + 1):
                    return True
        
        else:
            # Move to corresponding child node.
            child = node.child_node[ord(char) - ord("a")]
            # Child node exists and recursive call finds matches.
            if child and self.search_recursive(child, word, word_idx + 1):
                return True

        return False  # No valid paths are found.
