
class MaxFrequencyStack:  # LeetCode Q.895.
    def __init__(self):
        self.values2freqs: dict[int, int] = dict()
        # Each idx contains stack of values with frequency of idx + 1.
        self.freqs2stacks: list[list[int]] = []

    def push(self, value: int) -> None:
        if value not in self.values2freqs.keys():
            self.values2freqs.update({value: 0})
        self.values2freqs[value] += 1

        # Need to add another stack for current frequency.
        if self.values2freqs[value] > len(self.freqs2stacks):
            self.freqs2stacks.append([])
        self.freqs2stacks[self.values2freqs[value] - 1].append(value)

    def pop(self) -> int:
        most_freq_value = self.freqs2stacks[-1].pop(-1)
        self.values2freqs[most_freq_value] -= 1
        if not self.freqs2stacks[-1]:
            self.freqs2stacks.pop(-1)

        return most_freq_value
