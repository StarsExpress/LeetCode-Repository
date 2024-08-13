
def _get_permutation_string(self, round_idx: int, order: int):
    permutation_string = self.digits_str.pop(round_idx)
    self.digits_count -= 1
    if self.digits_count == 2:  # Only two digits remain.
        if order == 2:  # Swap remaining two digits.
            self.digits_str[-1], self.digits_str[-2] = self.digits_str[-2], self.digits_str[-1]
        return permutation_string + "".join(self.digits_str)

    round_idx = (order - 1) // self.factorials[self.digits_count - 1]
    order %= self.factorials[self.digits_count - 1]
    if order == 0:  # Points to last permutation of earlier round.
        order += self.factorials[self.digits_count - 1]

    return permutation_string + self._get_permutation_string(round_idx, order)


def find_kth_permutation(self, range_length: int, k: int):  # LeetCode Q.60.
    self.digits_str = [str(i) for i in range(1, range_length + 1)]
    self.digits_count = range_length

    if k == 1:  # Base case.
        return "".join(self.digits_str)
    if k == 2:  # Base case: swap remaining two digits.
        return "".join(self.digits_str[:-2]) + self.digits_str[-1] + self.digits_str[-2]

    self.factorials, factorial = dict(), 1  # Track factorials from 2 to n - 1.
    for i in range(2, range_length):
        factorial *= i
        self.factorials.update({i: factorial})

    # Round idx points to permutation's 1st digit.
    round_idx = (k - 1) // self.factorials[range_length - 1]
    order = k % self.factorials[range_length - 1]
    if order == 0:  # Points to last permutation of earlier round.
        order += self.factorials[range_length - 1]

    return self._get_permutation_string(round_idx, order)
