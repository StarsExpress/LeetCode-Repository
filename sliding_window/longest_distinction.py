
def find_longest_distinction(string: str):  # LeetCode Q.3.
    if len(string) <= 0:
        return 0
    if len(set(string)) == 1:
        return 1

    max_len, start_idx, end_idx = 1, 0, 1  # Iteration starts from 2nd char.
    while True:
        if end_idx >= len(string):  # Reach input's end.
            return max(end_idx - start_idx, max_len)

        # Candidate char is inside "somewhere" of window.
        if string[end_idx] in string[start_idx: end_idx]:
            max_len += max(end_idx - start_idx - max_len, 0)  # Update max length.
            # Candidate char's window location.
            start_idx += string[start_idx: end_idx].index(string[end_idx])
            start_idx += 1  # Now candidate char isn't in newest window.

        end_idx += 1  # Go to next char.
