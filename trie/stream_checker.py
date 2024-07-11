
total_letters = 26  # 26 lowercase letters.
min_letter = "a"


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class WordsTrie:
    """Words insertion & search."""

    def __init__(self, words: list[str]):
        self.root = TrieNode()
        self.letters_pool = set()  # Occurred letters in words list.
        self.max_len = 0  # Max length of words in list.
        for word in words:
            self._insert_word(word)

    def _insert_word(self, word: str):
        self.max_len = max(len(word), self.max_len)

        current_node = self.root
        for char in reversed(word):  # Insert word in reverse order.
            self.letters_pool.add(char)

            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                current_node.child_node[idx] = TrieNode()

            current_node = current_node.child_node[idx]

        current_node.word_end = True

    def search_reverse_letters(self, letters: list[str]):
        current_node = self.root
        for char in reversed(letters):
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                return False

            current_node = current_node.child_node[idx]
            if current_node.word_end:
                return True

        return False


class StreamChecker:  # LeetCode Q.1032.
    """Find out if current letters stream form a word in given words list."""

    def __init__(self, words: list[str]):
        self.words_trie = WordsTrie(words)
        self.stream_chars = []

    def query(self, letter: str) -> bool:
        if letter not in self.words_trie.letters_pool:
            self.stream_chars.clear()  # Reset stream if letter not in pool.
            return False

        self.stream_chars.append(letter)
        if len(self.stream_chars) > self.words_trie.max_len:
            self.stream_chars.pop(0)  # Limit stream max length.

        return self.words_trie.search_reverse_letters(self.stream_chars)
