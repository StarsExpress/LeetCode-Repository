
class TrieNode:
    def __init__(self) -> None:
        self.child_node: list[TrieNode | None] = [None] * 2  # 0 or 1 in bin num.
        self.prefix_count = 0  # Count of bin nums having prefix until this node.


class RangedXORPairs:  # LeetCode Q.1803.
    def __init__(self) -> None:
        self.trie, self.bin_nums = TrieNode(), []
        self.max_level = 0

    def _count_limited_pairs(self, xor_limit: int) -> int:
        if xor_limit >= 2 ** (self.max_level + 1) - 1:  # All pairs satisfy limit.
            return len(self.bin_nums) * (len(self.bin_nums) - 1) // 2

        limited_pairs = 0

        bin_limit = bin(xor_limit)[2:]  # Skip "0b" prefix. Pre-pad "0" to unify length.
        bin_limit = "0" * (self.max_level - len(bin_limit)) + bin_limit

        for bin_num in self.bin_nums:  # Find each bin num's count of complements.
            node = self.trie
            for idx, char in enumerate(bin_num):
                bit = int(char)
                if bin_limit[idx] == "1":
                    if node.child_node[bit]:
                        limited_pairs += node.child_node[bit].prefix_count

                    node = node.child_node[bit ^ 1]

                else:
                    node = node.child_node[bit]

                if node is None:  # No more satisfying complements among trie.
                    break

                if idx == self.max_level - 1:  # Have reached end of trie.
                    limited_pairs += node.prefix_count

            # A pair must be formed by nums[i] and nums[j] where i != j.
            limited_pairs -= 1  # Self xor = 0. Remove it from pairs.

        return limited_pairs // 2  # Remove duplicates.

    def _insert_num(self, bin_num: str) -> None:
        node = self.trie
        for char in bin_num:
            idx = int(char)
            if not node.child_node[idx]:
                node.child_node[idx] = TrieNode()

            node = node.child_node[idx]
            node.prefix_count += 1

    def count_ranged_pairs(self, nums: list[int], low: int, high: int) -> int:
        self.trie = [None] * 2  # Reset before counting.
        self.bin_nums.clear()
        self.max_level = len(bin(max(nums))) - 2  # Skip "0b" prefix.

        for num in nums:
            bin_num = bin(num)[2:]  # Skip "0b" prefix. Pre-pad "0" to unify length.
            bin_num = "0" * (self.max_level - len(bin_num)) + bin_num
            self.bin_nums.append(bin_num)
            self._insert_num(bin_num)

        return self._count_limited_pairs(high) - self._count_limited_pairs(low - 1)
