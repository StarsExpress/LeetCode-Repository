
total_letters = 26  # 26 lower cases.


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class SearchRecommender:  # LeetCode Q.1268.
    """Recommend searches with top 3 lex order as long as search word is found in trie"""

    def __init__(self, products: list[str]):
        self.root = TrieNode()
        for product in sorted(products):
            self._insert_word(product)

    def _insert_word(self, word: str):
        current_node = self.root
        for char in word:
            if not current_node.child_node[ord(char) - ord("a")]:
                current_node.child_node[ord(char) - ord("a")] = TrieNode()
            current_node = current_node.child_node[ord(char) - ord("a")]
        current_node.word_end = True

    def _search_node(self, word: str):
        current_node = self.root
        for char in word:
            if not current_node.child_node[ord(char) - ord("a")]:
                return None  # Return None if target word isn't among trie.

            current_node = current_node.child_node[ord(char) - ord("a")]

        return current_node

    def _dfs_word(self, current_node: TrieNode, word_prefix: str, sorted_words: list[str]):
        if current_node is None:
            return

        if len(sorted_words) >= 3:
            return

        if current_node.word_end:
            sorted_words.append(word_prefix)
            if len(sorted_words) >= 3:  # Only need top 3 lex order words
                return

        for i in range(total_letters):
            if current_node.child_node[i] is not None:
                self._dfs_word(current_node.child_node[i], word_prefix + chr(i + ord("a")), sorted_words)

    def recommend_searches(self, search_word: str):
        recommendations = []
        sorted_suggestions = []
        for i in range(1, len(search_word) + 1):
            last_node = self._search_node(search_word[:i])
            if last_node:
                self._dfs_word(last_node, search_word[:i], sorted_suggestions)
            recommendations.append(sorted_suggestions.copy())
            sorted_suggestions.clear()
        return recommendations
