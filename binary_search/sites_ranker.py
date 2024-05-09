
class SitesRanker:  # LeetCode Q.2102.
    """Rank sites with descending scores. For ties, rank by ascending names."""

    def __init__(self):
        self.names, self.scores, self.received_calls = [], [], 0  # Count of get_site method being called.

    def rank_score(self, score: int | float):
        if len(self.scores) <= 0:
            return 0

        back_idx, front_idx = 0, len(self.scores) - 1
        while True:
            if back_idx > front_idx:
                return back_idx

            mid_idx = (back_idx + front_idx) // 2
            if self.scores[mid_idx] > score:
                back_idx = mid_idx + 1
                continue

            front_idx = mid_idx - 1

    @staticmethod
    def rank_name(name: str, sorted_names: list[str]):
        if len(sorted_names) <= 0:
            return 0

        back_idx, front_idx = 0, len(sorted_names) - 1
        while True:
            if back_idx > front_idx:
                return back_idx

            mid_idx = (back_idx + front_idx) // 2
            if sorted_names[mid_idx] < name:
                back_idx = mid_idx + 1
                continue

            front_idx = mid_idx - 1

    def add_site(self, name: str, score: int):
        higher_count = self.rank_score(score)  # Count of past scores > new score.
        # Count of past scores >= new score. Scores are ints with descending ranks, -0.1 help find ties.
        higher_equal_count = self.rank_score(score - 0.1)
        if higher_count == higher_equal_count:  # No tie for new score.
            self.names.insert(higher_count, name)
            self.scores.insert(higher_count, score)
            return

        tied_names = self.names[higher_count: higher_equal_count]  # Tie: find names with scores = new score.
        # New name's rank among tied names = adjustment term for insertions.
        higher_count += self.rank_name(name, tied_names)
        self.names.insert(higher_count, name)
        self.scores.insert(higher_count, score)

    def get_site(self):
        self.received_calls += 1
        return self.names[self.received_calls - 1]
