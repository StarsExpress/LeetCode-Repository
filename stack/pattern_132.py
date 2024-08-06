
def find_132_pattern(integers: list[int]):  # LeetCode Q.456.
    stack = []  # Format: (interval min, interval max).
    for integer in integers:
        if not stack or integer < stack[-1][0]:  # Stack is empty or current int < interval min.
            stack.append([integer, integer])
            continue

        interval_min = stack[-1][0]  # Record interval min for later interval storage.
        while stack and stack[-1][1] < integer:  # Keep popping as long as interval max < current int.
            stack.pop()

        if stack and stack[-1][0] < integer < stack[-1][1]:
            return True
        stack.append([interval_min, integer])

    return False
