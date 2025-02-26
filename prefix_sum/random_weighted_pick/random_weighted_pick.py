from random import randrange


class RandomWeightedPick:  # LeetCode Q.528.
    def __init__(self, weights: list[int]):
        self.prefix_sums, self.total_candidates = [], len(weights)
        for weight in weights:
            if not self.prefix_sums:  # 1st weight.
                self.prefix_sums.append(weight)
                continue
            self.prefix_sums.append(self.prefix_sums[-1] + weight)

        self.pick_range_max = self.prefix_sums[-1]

    def make_pick(self) -> int:
        pick = randrange(1, self.pick_range_max + 1)  # Plus 1 to include range max.
        back_idx, front_idx = 0, self.total_candidates - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.prefix_sums[mid_idx] < pick:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of prefix sums < pick, implying selected candidate.
