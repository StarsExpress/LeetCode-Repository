
total_letters = 26  # 26 lower cases.
min_letter = "a"


class TrieNode:
    def __init__(self):
        self.child_node: list[TrieNode | None] = [None] * total_letters
        self.word_end = False  # If any word stops at this node.


class WordsReplacer:  # LeetCode Q.648.
    """
    Given a sentence, replace each word with its ancestor (sharing shortest prefix) among trie.
    If ancestor isn't found, keep the word as it is. Return modified sentence.
    """
    def __init__(self, dictionary: list[str]):
        self.root = TrieNode()
        for word in dictionary:
            self._insert_word(word)

    def _insert_word(self, word: str):
        current_node = self.root
        for char in word:
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:
                current_node.child_node[idx] = TrieNode()

            current_node = current_node.child_node[idx]

        current_node.word_end = True  # Last iterated node has word ending here.

    def _search_ancestor(self, word: str):
        current_node = self.root
        ancestor = ""
        for char in word:
            idx = ord(char) - ord(min_letter)
            if not current_node.child_node[idx]:  # Iterated char has no nodes in trie.
                return word  # No ancestor. Keep word as it is.

            ancestor += char  # Assemble visited chars into potential ancestor.
            current_node = current_node.child_node[idx]
            if current_node.word_end:
                return ancestor  # Ancestor found.

        return word  # No ancestor. Keep word as it is.

    def replace_words(self, sentence: str):
        words = sentence.split(" ")
        total_words = len(words)
        for _ in range(total_words):
            replaced_word = self._search_ancestor(words.pop(0))
            words.append(replaced_word)
        return " ".join(words)
