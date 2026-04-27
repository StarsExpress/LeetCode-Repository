
class MaxFrequencyStack:  # LeetCode Q.895.
    def __init__(self):
        self.vals2freqs: dict[int, int] = dict()

        # Each idx contains stack of values with frequency = idx + 1.
        self.freqs2stacks: list[list[int]] = []
    
    def push(self, value: int) -> None:
        if value not in self.vals2freqs.keys():
            self.vals2freqs.update({value: 0})
        self.vals2freqs[value] += 1
        
        # Need to add another stack for current frequency.
        if self.vals2freqs[value] > len(self.freqs2stacks):
            self.freqs2stacks.append([])
        
        self.freqs2stacks[self.vals2freqs[value] - 1].append(value)

    def pop(self) -> int:
        most_freq_val = self.freqs2stacks[-1].pop(-1)
        self.vals2freqs[most_freq_val] -= 1
        
        if not self.freqs2stacks[-1]: self.freqs2stacks.pop(-1)
        
        return most_freq_val
