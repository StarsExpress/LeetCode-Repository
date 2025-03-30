
class NonB2BOnesCounter:  # LeetCode Q.600.
    """
    Given a non-negative integer, return number of integers in the range
    [0, n] whose binary representations do not contain consecutive ones.
    """
    def __init__(self):
        self.non_b2b_ones_counts: dict[int, int] = {0: 1, 1: 2}  # Base case: num = 0 or 1.

    def count_non_b2b_ones(self, num: int) -> int:
        if num in self.non_b2b_ones_counts.keys():
            return self.non_b2b_ones_counts[num]

        bin_str = bin(num)[2:]  # Remove "0b" prefix.
        bin_level = len(bin_str)

        first_1_idx, second_1_idx = None, None
        for idx, char in enumerate(bin_str):
            if first_1_idx is None and char == "1":
                first_1_idx = idx
                continue
            if second_1_idx is None and char == "1":
                second_1_idx = idx
                break

        query_num = 2 ** (bin_level - 1 - first_1_idx) - 1
        self.non_b2b_ones_counts.update(
            {num: self.count_non_b2b_ones(query_num)}
        )

        if second_1_idx is None:  # Current num's bin form has only one 1 bit.
            self.non_b2b_ones_counts[num] += 1  # Min num at current num's bin level.
            return self.non_b2b_ones_counts[num]

        if first_1_idx + 1 == second_1_idx:  # Must reduce 1 level.
            query_num = 2 ** (bin_level - 1 - second_1_idx) - 1

        else:
            query_num = int(bin_str[second_1_idx:], 2)

        self.non_b2b_ones_counts[num] += self.count_non_b2b_ones(query_num)
        return self.non_b2b_ones_counts[num]
