from bisect import bisect_right


class SitesRanker:  # LeetCode Q.2102.
    def __init__(self) -> None:
        self.locations_scores = []  # Sorted in ascending score and name. Format: (negative score, name).
        self.query_calls = 0

    def add_site(self, name: str, score: int) -> None:
        idx = bisect_right(self.locations_scores, (-score, name))
        self.locations_scores.insert(idx, (-score, name))

    def get_site(self) -> str:
        self.query_calls += 1
        return self.locations_scores[self.query_calls - 1][1]
