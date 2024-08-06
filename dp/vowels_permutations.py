
class VowelsPermutaions:  # LeetCode Q.1220.
    def __init__(self):
        self.vowels_counts = {}

    def _store_counts(self):
        self.vowels_counts.clear()  # Reset before counting.
        self.vowels_counts.update({"a": 1, "e": 1, "i": 1, "o": 1, "u": 1})

    def count_permutations(self, n: int, recursion: bool = False) -> int:
        if not recursion:
            self._store_counts()
        if n == 1:  # Base case.
            return sum(self.vowels_counts.values())

        self.count_permutations(n - 1, True)
        latest_a_count = self.vowels_counts["a"]
        latest_e_count = self.vowels_counts["e"]
        latest_i_count = self.vowels_counts["i"]
        latest_o_count = self.vowels_counts["o"]
        latest_u_count = self.vowels_counts["u"]
        self.vowels_counts.update(
            {
                "a": latest_e_count,
                "e": latest_a_count + latest_i_count,
                "i": latest_a_count + latest_e_count + latest_o_count + latest_u_count,
                "o": latest_i_count + latest_u_count,
                "u": latest_a_count
            }
        )

        if not recursion:  # Required to control size.
            return sum(self.vowels_counts.values()) % (10 ** 9 + 7)
