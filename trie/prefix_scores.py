
total_letters = 26  # 26 lower cases.
min_letter = "a"


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.prefix_count = 0  # Count of words having prefix until this char node.


class PrefixScores:  # LeetCode Q.2416.
    """
    Given list of non-empty words, the score of words[i] is number of other words[j],
    where j != i, with words[i] as prefix.
    """
    def __init__(self):
        self.root = TrieNode()

    def calculate_scores(self, words: list[str]):
        for word in words:
            self._insert_word(word)

        scores = []
        while words:
            score = self._count_prefixes(words.pop(0))
            scores.append(score)
        return scores

    def _insert_word(self, word: str):
        current_node = self.root
        for char in word:
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                current_node.child_node[idx] = TrieNode()

            current_node = current_node.child_node[idx]
            current_node.prefix_count += 1  # Input word has prefix until current node.

    def _count_prefixes(self, word: str):
        prefixes_count = 0
        current_node = self.root
        for char in word:
            idx = ord(char) - ord(min_letter)
            current_node = current_node.child_node[idx]
            prefixes_count += current_node.prefix_count
        return prefixes_count
