
total_letters = 26  # 26 lower cases.


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class BasicTrie:
    """Word insertion, search & deletion."""

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

    def delete_word(self, word: str):
        current_node = self.root
        last_branch_node = None
        last_branch_char = "a"

        total_child_nodes = 0  # Iterated char's total child nodes.
        for char in word:
            if not current_node.child_node[ord(char) - ord("a")]:
                return  # Deleted word isn't among trie.

            total_child_nodes -= total_child_nodes  # Reset before calculation.
            for i in range(total_letters):
                if current_node.child_node[i]:
                    total_child_nodes += 1

            if total_child_nodes > 1:
                last_branch_node = current_node
                last_branch_char = char

            current_node = current_node.child_node[ord(char) - ord("a")]

        # Case 1: deleted word is a prefix of other words.
        if total_child_nodes > 0:
            current_node.word_end = False  # No more words stop at this node.
            return

        # Case 2: deleted word shares a common prefix with other words.
        if last_branch_node:
            last_branch_node.child_node[ord(last_branch_char) - ord("a")] = None
            return

        # Case 3: deleted word doesn't share any common prefix with other words.
        self.root.child_node[ord(word[0]) - ord("a")] = None
        return