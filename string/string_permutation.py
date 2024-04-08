
def seek_permutation(substring: str, string: str):  # LeetCode Q.567.
    window_size = len(substring)  # Substring decides window size.
    if min(window_size, len(string)) <= 0:
        return False
    if len(string) < window_size:
        return False

    substr_chars, counts_table = list(substring), dict()
    for char in substr_chars:  # Each substring's char count.
        if char not in counts_table.keys():
            counts_table.update({char: 0})
        counts_table[char] += 1

    # Map each substring's char to a unique idx.
    substr_idx_table = dict(zip(list(counts_table.keys()), [i for i in range(len(counts_table))]))

    # Substring's chars counts all <= 0: implies permutation.
    substr_counts = list(counts_table.values())

    window = string[:window_size]  # First window.
    for char in window:
        if char in substr_idx_table.keys():
            substr_counts[substr_idx_table[char]] -= 1

    if max(substr_counts) == 0:
        return True

    current_idx = window_size
    while True:
        if current_idx >= len(string):
            return False

        # The char thrown out of window in current iteration.
        if string[current_idx - window_size] in substr_idx_table.keys():
            # Its window count rises by 1.
            substr_counts[substr_idx_table[string[current_idx - window_size]]] += 1

        # The char joining window in current iteration.
        if string[current_idx] in substr_idx_table.keys():
            # Its window count drops by 1.
            substr_counts[substr_idx_table[string[current_idx]]] -= 1

        if max(substr_counts) == 0:  # All substring's chars are covered.
            return True

        current_idx += 1
