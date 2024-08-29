
def find_largest_substring(string: str):  # LeetCode Q.1163.
    """Find substring with the largest lex order."""
    largest_substring = string  # Base case.
    start_idx, s_len = 1, len(string)
    while start_idx < s_len:
        if string[start_idx] >= largest_substring[0]:  # Current substring might win.
            current_substring = string[start_idx:]
            if current_substring > largest_substring:
                largest_substring = current_substring

        start_idx += 1

    return largest_substring
