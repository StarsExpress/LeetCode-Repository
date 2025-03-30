
class LongestNonRepeatingPath:  # LeetCode Q.2246.
    def __init__(self):
        self.string = ""
        self.tree: dict[int, list[int]] = dict()
        self.max_non_repeating_len = 1  # Base case.

    def find_longest_non_repeating_len(self, parent: list[int], string: str) -> int:
        self.string = string
        self.tree.clear()
        for child_idx, parent_idx in enumerate(parent):
            if parent_idx != -1:  # Non root nodes.
                if parent_idx not in self.tree.keys():
                    self.tree.update({parent_idx: []})
                self.tree[parent_idx].append(child_idx)

        self.max_non_repeating_len = 1  # Base case.
        self._dfs_max_non_repeating_len(0)  # Start from root.
        return self.max_non_repeating_len

    def _dfs_max_non_repeating_len(self, idx: int) -> int:
        if idx not in self.tree.keys():  # Base case: leave nodes.
            return 1

        top_2_children_lens = []
        for child_idx in self.tree[idx]:
            top_2_children_lens.append(0)  # Default to 0.

            children_len = self._dfs_max_non_repeating_len(child_idx)
            if self.string[child_idx] != self.string[idx]:
                top_2_children_lens[-1] += children_len

            if len(top_2_children_lens) > 2:  # Always keep top 2.
                top_2_children_lens.sort(reverse=True)
                top_2_children_lens.pop(-1)

        straight_len = 1 + max(top_2_children_lens)
        # Curve path is centered at current node.
        curve_len = 1 + sum(top_2_children_lens)

        if max(straight_len, curve_len) > self.max_non_repeating_len:
            self.max_non_repeating_len = max(straight_len, curve_len)

        return straight_len  # Only straight len can be reported to parent.
