
class SitesRanker:  # LeetCode Q.2102.
    """Rank sites with descending scores. For ties, rank by ascending names."""
    def __init__(self):
        self.names, self.scores = [], []
        self.received_calls = 0  # Count of get_site method being called.

    def _rank_score(self, score: int | float):
        if not self.scores:
            return 0

        back_idx, front_idx = 0, len(self.scores) - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.scores[mid_idx] > score:  # Scores have descendant ranks.
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx

    @staticmethod
    def _rank_name(name: str, sorted_names: list[str]):
        if not sorted_names:
            return 0

        back_idx, front_idx = 0, len(sorted_names) - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if sorted_names[mid_idx] < name:  # Tied scores: names have ascendant ranks.
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx

    def add_site(self, name: str, score: int):
        higher_count = self._rank_score(score)  # Count of past scores > new score.

        # Count of past scores >= new score. Scores are ints with descending ranks.
        higher_or_equal_count = self._rank_score(score - 0.1)  # -0.1 help find ties.

        if higher_count == higher_or_equal_count:  # No tie for new score.
            self.names.insert(higher_count, name)
            self.scores.insert(higher_count, score)
            return

        # Tie: find existing names with scores = new score.
        tied_names = self.names[higher_count: higher_or_equal_count]
        # New name's rank among tied names = extra term for insertion idx.
        higher_count += self._rank_name(name, tied_names)
        self.names.insert(higher_count, name)
        self.scores.insert(higher_count, score)

    def get_site(self):
        self.received_calls += 1
        return self.names[self.received_calls - 1]
