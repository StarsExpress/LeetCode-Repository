
def find_min_substring(mother_str: str, target_str: str) -> str:  # LeetCode Q.76.
    total_uncovered_chars = len(target_str)
    chars2counts: dict[str, int] = dict()
    for char in target_str:
        if char not in chars2counts.keys():
            chars2counts.update({char: 0})
        chars2counts[char] += 1

    min_substring = ""
    substring_start_idx, min_len = -1, float("inf")

    left_idx = 0
    for right_idx, right_char in enumerate(mother_str):
        if right_char in chars2counts.keys():
            if chars2counts[right_char] > 0:
                total_uncovered_chars -= 1
            chars2counts[right_char] -= 1

            while total_uncovered_chars == 0:
                substring_len = right_idx + 1 - left_idx
                if substring_len < min_len:
                    min_len = substring_len
                    substring_start_idx = left_idx

                if mother_str[left_idx] in chars2counts.keys():
                    if chars2counts[mother_str[left_idx]] == 0:
                        break
                    chars2counts[mother_str[left_idx]] += 1

                left_idx += 1

    if substring_start_idx != -1:
        min_substring += mother_str[substring_start_idx: substring_start_idx + min_len]
    return min_substring
