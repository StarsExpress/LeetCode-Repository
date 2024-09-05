
def generate_parentheses(pairs: int) -> list[str]:  # LeetCode Q.22.
    parentheses = []

    # Track counts of left side and right side parenthesis.
    def recursion(left_count: int, right_count: int, parenthesis: str):
        if left_count == right_count == pairs:  # Base case: reach max number of parentheses pairs.
            parentheses.append(parenthesis)
            return

        if left_count < pairs:  # Add left parenthesis if its count < pairs.
            recursion(left_count + 1, right_count, parenthesis + '(')

        if left_count > right_count:  # Add right parenthesis if its count < that of left.
            recursion(left_count, right_count + 1, parenthesis + ')')

    recursion(0, 0, '')
    return parentheses
