
class SitesRanker:  # LeetCode Q.2102.
    """Rule: rank ascending "negative" scores and names."""

    def __init__(self) -> None:
        self.negative_scores_and_names, self.size = [], 0
        self.received_calls = 0  # Count of get method being called.

    def add_site(self, name: str, score: int) -> None:
        left_idx, right_idx = 0, self.size - 1  # Back idx is also insertion idx.
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if self.negative_scores_and_names[mid_idx] < (-score, name):
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        self.negative_scores_and_names.insert(left_idx, (-score, name))
        self.size += 1

    def get_site(self) -> str:
        self.received_calls += 1
        return self.negative_scores_and_names[self.received_calls - 1][1]
