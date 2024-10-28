
class NoB2BOnesIntegersCounter:  # LeetCode Q.600.
    """
    Given a positive integer, return number of integers in the range
    [0, n] whose binary representations do not contain consecutive ones.
    """
    def _open_table(self) -> None:
        # Key: binary format level.
        # Value: count of integers in the range [0, 2 ** key - 1] w/o back-to-back ones.
        self.levels_cumulated_counts = {1: 2, 2: 3}

    def count_no_back2back_ones(self, integer: int, recursive: bool = False) -> int:
        if integer <= 2:  # Base case.
            return integer + 1
        if integer == 3:  # Base case.
            return 3

        if not recursive:
            self._open_table()

        int_bin = bin(integer)[2:]  # Don't include substring "0b".
        current_level = len(int_bin)

        if current_level - 1 not in self.levels_cumulated_counts.keys():
            self.count_no_back2back_ones(2 ** (current_level - 1) - 1, True)
        last_level_cumulated_count = self.levels_cumulated_counts[current_level - 1]

        current_level_min = 2 ** (current_level - 1)
        if integer == current_level_min:  # Bin format "10...0" (input int = 2 ** x).
            return last_level_cumulated_count + 1

        if integer == current_level_min + 1:  # Bin format "10...1" (input int = 2 ** x + 1).
            return last_level_cumulated_count + 2

        for idx, char in enumerate(int_bin):  # Look for remaining count at current bin level.
            if idx > 0 and char == "1":  # Find the 2nd "1" in bin format.
                if idx == 1:  # Bin format "11...".
                    if current_level - 1 - idx not in self.levels_cumulated_counts.keys():
                        self.count_no_back2back_ones(
                            2 ** (current_level - idx) - 1, True
                        )

                    remaining_count = self.levels_cumulated_counts[current_level - 1 - idx]
                    # Recursive calls only give ints of 2 ** x - 1.
                    self.levels_cumulated_counts.update(
                        {current_level: last_level_cumulated_count + remaining_count}
                    )
                    return last_level_cumulated_count + remaining_count

                # Bin format "10...1...".
                remaining_count = self.count_no_back2back_ones(int(int_bin[idx:], 2), True)
                return last_level_cumulated_count + remaining_count
