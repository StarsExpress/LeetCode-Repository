
def seek_string_remains(string: str):  # LeetCode Q.3039.
    if len(string) <= 1:
        return string

    # Track each char's count and its last occurred idx.
    chars, counts_table, last_indices_table = list(string), dict(), dict()
    for idx, char in enumerate(chars):
        if char not in counts_table.keys():
            counts_table.update({char: 0})

        counts_table[char] += 1
        last_indices_table.update({char: idx})

    # Last remaining chars must have the highest count.
    max_count, remaining_chars_indices = max(counts_table.values()), []
    for char, count in counts_table.items():
        if count == max_count:  # Find remaining char's last occurred idx.
            remaining_chars_indices.append(last_indices_table[char])

    remaining_chars_indices.sort()  # Sort by last occurred idx and concat string.
    return ''.join(chars[idx] for idx in remaining_chars_indices)
