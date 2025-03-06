
class TrieNode:
    def __init__(self) -> None:
        self.child_node: list[TrieNode | None] = [None] * 2  # 0 or 1 in bin num.


class MaxXOR:
    def __init__(self):
        self.root, self.min_char = TrieNode(), "0"

    def _insert_num(self, bin_num: str) -> None:
        node = self.root
        for char in bin_num:
            idx = ord(char) - ord(self.min_char)
            if not node.child_node[idx]:
                node.child_node[idx] = TrieNode()

            node = node.child_node[idx]

    def find_max_xor(self, nums: list[int]) -> int:  # LeetCode Q.421.
        nums = set(nums)  # Remove duplicates.
        max_level = len(bin(max(nums))) - 2  # Skip "0b" prefix.
        max_level_bin_nums = []  # Search w.r.t. bin nums at max level.

        self.root.child_node = [None] * 2  # Reset trie.
        for num in nums:
            bin_num = bin(num)[2:]  # Skip "0b" prefix.
            if len(bin_num) == max_level:
                max_level_bin_nums.append(bin_num)

            self._insert_num(  # Pre-pad "0" to unify length.
                "0" * (max_level - len(bin_num)) + bin_num
            )

        max_xor = 0
        for bin_num in max_level_bin_nums:
            xor_str, node = "", self.root
            for char in bin_num:
                complement_idx = ord(str(int(char) ^ 1)) - ord(self.min_char)
                if node.child_node[complement_idx]:
                    xor_str += "1"  # 1 means complement char exists.
                    node = node.child_node[complement_idx]

                else:
                    xor_str += "0"  # 1 means no complement char found.
                    node = node.child_node[ord(char) - ord(self.min_char)]

            xor = int(xor_str, 2)
            if xor > max_xor:
                max_xor = xor

        return max_xor
