
def find_min_window_substring(source_str: str, target_str: str) -> str:  # LeetCode Q.76.
    tgt_chars_counts: dict[str, int] = dict()

    for char in target_str:
        if char not in tgt_chars_counts.keys():
            tgt_chars_counts.update({char: 0})
        tgt_chars_counts[char] += 1

    unique_tgt_chars_count = len(tgt_chars_counts)

    # Must not exceed unique target chars count during sliding window.
    coverage = 0

    min_window_left_idx = -1
    min_len = len(source_str) + 1  # Source length + 1: symbol of not found yet.

    left_idx = 0
    for right_idx, char in enumerate(source_str):
        if char in tgt_chars_counts.keys():
            tgt_chars_counts[char] -= 1

            if tgt_chars_counts[char] == 0:  # Becomes covered.
                coverage += 1

        while coverage == unique_tgt_chars_count:  # Can try to shrink window.
            window_len = right_idx + 1 - left_idx

            if window_len < min_len:
                min_len = window_len
                min_window_left_idx = left_idx

            removed_char = source_str[left_idx]
            if removed_char in tgt_chars_counts.keys():
                tgt_chars_counts[removed_char] += 1

                if tgt_chars_counts[removed_char] > 0:  # Becomes uncovered.
                    coverage -= 1

            left_idx += 1

    if min_len == len(source_str) + 1: return ""

    return source_str[min_window_left_idx: min_window_left_idx + min_len]
