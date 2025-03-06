
class TrieNode:
    def __init__(self) -> None:
        self.child_node: list[TrieNode | None] = [None] * 2  # 0 or 1 in bin num.


class MaxLimitedXOR:  # LeetCode Q.1707.
    def __init__(self) -> None:
        self.root, self.min_char = TrieNode(), "0"

    def _insert_num(self, bin_num: str) -> None:
        node = self.root
        for char in bin_num:
            idx = int(char)
            if not node.child_node[idx]:
                node.child_node[idx] = TrieNode()

            node = node.child_node[idx]

    def find_max_limited_xor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        self.root.child_node = [None] * 2  # Reset trie.

        nums = sorted(set(nums))  # Remove duplicates.
        max_query_num = max(num for num, _ in queries)
        max_level = len(bin(max(max_query_num, nums[-1]))) - 2  # Skip "0b" prefix.

        queries = [(idx, query[0], query[1]) for idx, query in enumerate(queries)]
        queries.sort(key=lambda x: x[2])  # Sort by ascending limits.
        max_xor_results = [-1] * len(queries)

        for query_idx, query_num, query_limit in queries:
            while nums and nums[0] <= query_limit:
                bin_candidate_num = bin(nums.pop(0))[2:]  # Skip "0b" prefix.
                self._insert_num(  # Pre-pad "0" to unify length.
                    "0" * (max_level - len(bin_candidate_num)) + bin_candidate_num
                )

            if self.root.child_node != [None] * 2:  # Trie has numbers <= limit.
                node, xor_str = self.root, ""

                bin_num = bin(query_num)[2:]  # Skip "0b" prefix.
                bin_num = "0" * (max_level - len(bin_num)) + bin_num

                for idx, char in enumerate(bin_num):
                    complement_idx = int(char) ^ 1
                    if node.child_node[complement_idx]:
                        xor_str += "1"
                        node = node.child_node[complement_idx]

                    else:
                        xor_str += "0"
                        node = node.child_node[int(char)]

                max_xor_results[query_idx] = int(xor_str, 2)

        return max_xor_results
