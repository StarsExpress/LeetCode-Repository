
class TrieNode:
    def __init__(self) -> None:
        self.child_node: list[TrieNode | None] = [None] * 2  # 0 or 1 in bin str.
        self.bin_str_end = False  # If any bin str stops at this node.


def _insert_bin_str(self, bin_str: str) -> None:
    node = self.root
    for char in bin_str:
        idx = ord(char) - ord(self.min_char)
        if not node.child_node[idx]:  # Iterated char hasn't had a node in trie.
            node.child_node[idx] = TrieNode()  # Open a new node for this char.

        node = node.child_node[idx]  # Move to iterated char's node.

    node.bin_str_end = True  # Last iterated node has a bin str ending here.


def find_max_xor(self, numbers: list[int]) -> int:  # LeetCode Q.421.
    numbers = list(set(numbers))  # Remove duplicates.
    self.root = TrieNode()
    self.min_char = "0"

    max_level = len(bin(max(numbers))[2:])
    max_level_bin_strings = []  # Search w.r.t. bin strings at max level.
    for number in numbers:
        bin_str = bin(number)[2:]  # Skip "0b" substring.
        if len(bin_str) == max_level:
            max_level_bin_strings.append(bin_str)

        self._insert_bin_str(  # Pre-pad "0" to unify length.
            "0" * (max_level - len(bin_str)) + bin_str
        )

    max_xor = 0
    for bin_str in max_level_bin_strings:
        xor_str, node = "", self.root
        for char in bin_str:
            complement_char = "1" if char == "0" else "0"
            complement_idx = ord(complement_char) - ord(self.min_char)
            if node.child_node[complement_idx]:  # Current char has complement in trie.
                xor_str += "1"  # 1 means complement char exists.
                node = node.child_node[complement_idx]

            else:
                xor_str += "0"  # 1 means no complement char found.
                node = node.child_node[ord(char) - ord(self.min_char)]

        xor = int(xor_str, 2)
        if xor > max_xor:
            max_xor = xor

    return max_xor
