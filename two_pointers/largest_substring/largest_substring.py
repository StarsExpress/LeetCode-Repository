
def find_largest_substring(string: str) -> str:  # LeetCode Q.1163.
    """Find substring with the largest lex order."""
    start_idx = 0  # Start idx of the substring with max lexi order.
    # Current idx's char compares to (start idx + relative order) idx's char.
    relative_order = 0

    for idx in range(1, len(string)):
        if string[idx] == string[start_idx + relative_order]:
            relative_order += 1  # Tie: increment order to keep comparison.
            continue

        if string[idx] > string[start_idx]:  # Directly beats char at start idx.
            start_idx = idx

        elif string[idx] > string[start_idx + relative_order]:
            start_idx = idx - 1
            while string[start_idx - 1] >= string[start_idx]:
                start_idx -= 1  # Extend w.r.t. monotonicity.

        relative_order = 0  # Reset.

    return string[start_idx:]
