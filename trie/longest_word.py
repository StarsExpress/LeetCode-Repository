
total_letters = 26  # 26 lower cases.
min_letter = "a"


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class LongestWord:  # LeetCode Q.720.
    """Among list of words, return longest word that can be built one character at a time by other words.

    If there is more than one possible answer, return longest word with the smallest lex order.
    If there is no answer, return empty string."""

    def __init__(self, words: list[str]):
        self.root = TrieNode()
        while words:
            self._insert_word(words.pop())

    def find_longest_word(self):
        longest_word = {"word": "", "length": 0}
        self._dfs_descendants(self.root, "", longest_word)
        return longest_word["word"]

    def _insert_word(self, word: str):
        current_node = self.root
        for char in word:
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                current_node.child_node[idx] = TrieNode()

            current_node = current_node.child_node[idx]

        current_node.word_end = True

    def _dfs_descendants(
        self, starting_node: TrieNode, word_prefix: str, longest_word: dict[str, str | int],
    ):
        """
        Given a starting node and its word prefix,
        find the longest descendant that is also a word in words list.
        """
        if starting_node.word_end:  # Node is end of word.
            if len(word_prefix) > longest_word["length"]:
                longest_word.update(
                    {"word": word_prefix, "length": len(word_prefix)}
                )

        for i in range(total_letters):  # Recursively visit child nodes in lex order.
            if starting_node.child_node[i]:  # Child node exists.
                if starting_node.child_node[i].word_end:  # Child node is end of word.
                    self._dfs_descendants(
                        starting_node.child_node[i],
                        word_prefix + chr(i + ord(min_letter)),
                        longest_word,
                    )
