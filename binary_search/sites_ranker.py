
class SitesRanker:  # LeetCode Q.2102.
    """Rule: rank ascending "negative" scores and names."""
    def __init__(self) -> None:
        self.negative_scores_and_names, self.size = [], 0
        self.received_calls = 0  # Count of get method being called.

    def add_site(self, name: str, score: int) -> None:
        back_idx, front_idx = 0, self.size - 1  # Back idx is also insertion idx.
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.negative_scores_and_names[mid_idx] < (-score, name):
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        self.negative_scores_and_names.insert(back_idx, (-score, name))
        self.size += 1

    def get_site(self) -> str:
        self.received_calls += 1
        return self.negative_scores_and_names[self.received_calls - 1][1]
