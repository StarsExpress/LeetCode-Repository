
class SitesRanker:  # LeetCode Q.2102.
    """Rank sites with descending scores. For ties, rank by ascending names."""

    def __init__(self):
        self.names, self.scores = [], []
        self.received_calls = 0  # Count of get method being called.

    def rank_score(self, score: int, inclusive=False):
        if len(self.scores) <= 0:
            return 0

        back_idx, front_idx = 0, len(self.scores) - 1
        while True:
            if back_idx > front_idx:
                return back_idx

            mid_idx = (back_idx + front_idx) // 2
            if inclusive:  # Add equal sign in comparison.
                if self.scores[mid_idx] >= score:
                    back_idx = mid_idx + 1
                    continue

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
        ordinary_idx = self.rank_score(score)
        inclusive_idx = self.rank_score(score, True)
        if ordinary_idx == inclusive_idx:  # No tie for incoming score.
            self.names.insert(ordinary_idx, name)
            self.scores.insert(ordinary_idx, score)
            return

        # Tie happens: get names with scores equal to incoming score.
        tied_names = self.names[ordinary_idx: inclusive_idx]
        name_idx = self.rank_name(name, tied_names)  # Incoming name's rank among tied names.
        self.names.insert(ordinary_idx + name_idx, name)  # Name idx: adjustment term for both insertions.
        self.scores.insert(ordinary_idx + name_idx, score)

    def get_site(self):
        self.received_calls += 1
        return self.names[self.received_calls - 1]
