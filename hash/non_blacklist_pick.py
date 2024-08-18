from random import randrange


class NonBlacklistPick:
    """
    Pick a random integer in range [0, n - 1] that is not in blacklist.
    Blacklist is a list of unique integers in range [0, n - 1]. List size < n.
    """
    def __init__(self, n: int, blacklist: list[int]):
        self.selectable_count = n - len(blacklist)
        self.mapping_table = dict()

        for black_num in blacklist:
            self.mapping_table.update({black_num: 0})

        open_value = n - 1  # Mapping values drop monotonically from n - 1.
        for black_num in blacklist:
            if black_num < self.selectable_count:
                # Open value can't be black number (keys), nor can it be already used (values).
                while open_value in self.mapping_table:
                    open_value -= 1

                self.mapping_table[black_num] += open_value
                open_value -= 1  # Decrement for next black number.

    def pick(self) -> int:
        selection = randrange(self.selectable_count)
        if selection in self.mapping_table.keys():
            return self.mapping_table[selection]
        return selection
