
class MinStack:  # LeetCode Q.155.
    """Add & remove integers and find minimum within stack."""
    def __init__(self) -> None:
        self.stack, self.min_stack = [], []

    def push(self, integer: int) -> None:
        self.stack.append(integer)
        latest_min = min(integer, self.min_stack[-1]) if self.min_stack else integer
        self.min_stack.append(latest_min)

    def pop_top(self) -> None:
        self.stack.pop(-1)
        self.min_stack.pop(-1)

    def get_top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]
