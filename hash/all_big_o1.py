
class AllBigO1:  # LeetCode Q.432.
    def __init__(self) -> None:
        self.keys2counts: dict[str, int] = dict()
        self.counts2keys: dict[int, dict[str, bool]] = dict()

    def increment(self, key: str) -> None:
        if key not in self.keys2counts.keys():
            self.keys2counts.update({key: 0})

        else:  # Remove old count.
            old_count = self.keys2counts[key]
            del self.counts2keys[old_count][key]
            if not self.counts2keys[old_count]:
                del self.counts2keys[old_count]

        self.keys2counts[key] += 1  # This is new count.
        new_count = self.keys2counts[key]

        if new_count not in self.counts2keys.keys():
            self.counts2keys.update({new_count: dict()})
        self.counts2keys[new_count].update({key: True})

    def decrement(self, key: str) -> None:
        old_count = self.keys2counts[key]
        del self.counts2keys[old_count][key]
        if not self.counts2keys[old_count]:
            del self.counts2keys[old_count]

        self.keys2counts[key] -= 1  # This is new count.
        if self.keys2counts[key] == 0:
            del self.keys2counts[key]
            return

        new_count = self.keys2counts[key]
        if new_count not in self.counts2keys.keys():
            self.counts2keys.update({new_count: dict()})
        self.counts2keys[new_count].update({key: True})

    def get_max_key(self) -> str:
        if not self.keys2counts:  # No key has max count.
            return ""
        max_count = max(self.counts2keys.keys())  # Answer found.
        return list(self.counts2keys[max_count].keys())[0]

    def get_min_key(self) -> str:
        if not self.keys2counts:  # No key has min count.
            return ""
        min_count = min(self.counts2keys.keys())  # Answer found.
        return list(self.counts2keys[min_count].keys())[0]
