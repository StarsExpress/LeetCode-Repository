from random import randrange


class UnBlockedPick:  # LeetCode Q.710.
    """
    Pick a random integer in range [0, n - 1] that is not blocked.
    Blocked list is a list of unique integers in range [0, n - 1]. List size < n.
    """
    def __init__(self, n: int, blocked_nums: list[int]):
        self.total_candidates = n - len(blocked_nums)
        # Initialize replacements by -1.
        self.nums2replacements = dict(zip(blocked_nums, [-1] * len(blocked_nums)))

        replacement = self.total_candidates
        for blocked_num in blocked_nums:  # Need replacements for blocked nums in [0, total candidates - 1].
            if blocked_num < self.total_candidates:
                while replacement in self.nums2replacements.keys():
                    replacement += 1

                self.nums2replacements.update({blocked_num: replacement})
                replacement += 1

    def pick(self) -> int:
        picked_num = randrange(self.total_candidates)
        if picked_num in self.nums2replacements.keys():
            picked_num = self.nums2replacements[picked_num]

        return picked_num
