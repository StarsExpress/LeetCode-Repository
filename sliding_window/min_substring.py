
def find_min_substring(mother_str: str, target_str: str) -> str:  # LeetCode Q.76.
    min_substring, min_len = "", float("inf")

    chars2uncovered_counts, total_uncovered_count = dict(), 0
    for char in target_str:
        if char not in chars2uncovered_counts.keys():
            chars2uncovered_counts.update({char: 0})
        chars2uncovered_counts[char] += 1
        total_uncovered_count += 1

    left_idx, right_idx, s_len = 0, 0, len(mother_str)
    while right_idx < s_len:
        if mother_str[right_idx] in chars2uncovered_counts.keys():
            chars2uncovered_counts[mother_str[right_idx]] -= 1
            if chars2uncovered_counts[mother_str[right_idx]] >= 0:  # This char is in coverage process.
                total_uncovered_count -= 1

        if total_uncovered_count == 0:  # Current window fully covers the target substring.
            while left_idx <= right_idx:
                if mother_str[left_idx] in chars2uncovered_counts.keys():
                    if chars2uncovered_counts[mother_str[left_idx]] == 0:  # Can't move left idx forward.
                        break
                    chars2uncovered_counts[mother_str[left_idx]] += 1

                left_idx += 1

            current_len = right_idx - left_idx + 1
            if current_len < min_len:
                min_substring = mother_str[left_idx: right_idx + 1]
                min_len = current_len

        right_idx += 1

    return min_substring
