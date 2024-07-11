
total_letters = 26  # 26 lower cases.
min_letter = "a"


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class SearchRecommender:  # LeetCode Q.1268.
    """
    During typing target word, recommend searches of top 3 lex order
    if target word is found inside trie.
    """

    def __init__(self, available_words: list[str]):
        self.root = TrieNode()
        for word in sorted(available_words):
            self._insert_word(word)

    def _insert_word(self, word: str):
        current_node = self.root
        for char in word:
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                current_node.child_node[idx] = TrieNode()

            current_node = current_node.child_node[idx]

        current_node.word_end = True

    def _search_last_node(self, word: str):
        """Given a word, find its last node among trie."""
        current_node = self.root
        for char in word:
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                return None  # Return None if word isn't among trie.

            current_node = current_node.child_node[idx]

        return current_node

    def _dfs_descendants(
            self, starting_node: TrieNode, word_prefix: str, sorted_words: list[str]
    ):
        """Given a starting node, find descendants of top 3 lex order."""
        if len(sorted_words) >= 3:  # Only need top 3 words.
            return

        if starting_node.word_end:
            sorted_words.append(word_prefix)

        for i in range(total_letters):
            if starting_node.child_node[i] is not None:
                self._dfs_descendants(
                    starting_node.child_node[i],
                    word_prefix + chr(i + ord(min_letter)),
                    sorted_words
                )

    def recommend_searches(self, search_word: str):
        all_recommendations = []  # Suggestions during typing process.
        iterated_suggestions = []  # Suggestions for each updated search word.

        for i in range(1, len(search_word) + 1):
            last_node = self._search_last_node(search_word[:i])
            if last_node:  # Potential matches exist.
                self._dfs_descendants(last_node, search_word[:i], iterated_suggestions)

            all_recommendations.append(iterated_suggestions.copy())
            iterated_suggestions.clear()

        return all_recommendations
