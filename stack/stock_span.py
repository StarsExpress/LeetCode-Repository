
class StockSpanner:  # LeetCode Q.901.
    def __init__(self) -> None:
        self.stock_stack = []

    def find_span(self, price: int) -> int:
        stack_size = len(self.stock_stack)
        if stack_size <= 0:
            self.stock_stack.append((price, 1))
            return 1

        stack_idx, past_span = -1, 0
        while stack_idx >= -stack_size:
            if self.stock_stack[stack_idx][0] > price:
                break
            past_span += self.stock_stack[stack_idx][1]
            stack_idx -= self.stock_stack[stack_idx][1]

        self.stock_stack.append((price, past_span + 1))
        return past_span + 1
