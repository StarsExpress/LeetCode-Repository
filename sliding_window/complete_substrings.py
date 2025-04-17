
# a => 0, b => 1, ......, z => 25.
chars2indices = {chr(idx): idx - 97 for idx in range(97, 123)}

def _count_substrings(word: str, k: int, window_size: int) -> int:
    search_ranges: list[tuple[int, int]] = []

    start_idx = 0
    for end_idx, char in enumerate(word):
        if end_idx > 0 and abs(ord(char) - ord(word[end_idx - 1])) > 2:
            if end_idx - start_idx >= window_size:
                search_ranges.append((start_idx, end_idx - 1))

            start_idx = end_idx

        if end_idx == len(word) - 1 and end_idx + 1 - start_idx >= window_size:
            search_ranges.append((start_idx, end_idx))

    total_substrings = 0
    for range_start_idx, range_end_idx in search_ranges:
        chars2counts = [0] * 26
        counts2occurrences = [0] * (k + 1)  # Each idx i stores occurrences of count i.

        left_idx = range_start_idx
        for right_idx in range(range_start_idx, range_end_idx + 1):
            right_char_idx = chars2indices[word[right_idx]]

            if right_idx + 1 - left_idx > window_size:
                left_char_idx = chars2indices[word[left_idx]]
                chars2counts[left_char_idx] -= 1

                left_char_new_count = chars2counts[left_char_idx]
                counts2occurrences[left_char_new_count + 1] -= 1
                counts2occurrences[left_char_new_count] += 1
                left_idx += 1

            right_char_old_count = chars2counts[right_char_idx]
            counts2occurrences[right_char_old_count] -= 1

            chars2counts[right_char_idx] += 1
            if chars2counts[right_char_idx] <= k:
                right_char_new_count = chars2counts[right_char_idx]
                counts2occurrences[right_char_new_count] += 1

            else:
                while chars2counts[right_char_idx] > k:
                    left_char_idx = chars2indices[word[left_idx]]
                    chars2counts[left_char_idx] -= 1

                    left_char_new_count = chars2counts[left_char_idx]
                    if left_char_new_count + 1 <= k:
                        counts2occurrences[left_char_new_count + 1] -= 1

                    counts2occurrences[left_char_new_count] += 1
                    left_idx += 1

            if k * counts2occurrences[k] == window_size:
                total_substrings += 1

    return total_substrings


def count_complete_substrings(word: str, k: int) -> int:  # LeetCode Q.2953.
    if len(set(word)) == 1 and k == 1:
        return len(word)

    total_substrings = 0
    max_window_size = k * min(len(word) // k, 26)
    for window_size in range(k, max_window_size + 1, k):
        total_substrings += _count_substrings(word, k, window_size)

    return total_substrings
