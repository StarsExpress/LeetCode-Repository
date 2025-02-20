
def count_distinct_subsequences(sample: str, target: str) -> int:  # LeetCode Q.115.
    len_s, len_t = len(sample), len(target)
    if len_s < len_t:  # Base case: impossible to form target from sample.
        return 0

    chars2roles: dict[str, list[int]] = dict()
    for reverse_idx, char in enumerate(target[::-1]):  # Backward: put descending roles.
        if char not in chars2roles.keys():
            chars2roles.update({char: []})
        chars2roles[char].append(len_t - reverse_idx)  # Role = len(target) - reverse idx.

    progress_counts: dict[int, int] = dict()
    for char in sample:
        if char in chars2roles.keys():
            for role in chars2roles[char]:
                if role not in progress_counts.keys():
                    progress_counts.update({role: 0})

                if role == 1:  # Opens a possible subseq start of progress 1.
                    progress_counts[1] += 1

                # Extends subseqs w/ 1 < pregress < len(target) - 1.
                # Fulfills subseqs w/ pregress at len(target) - 1.
                if role - 1 in progress_counts.keys():
                    progress_counts[role] += progress_counts[role - 1]

    return 0 if len_t not in progress_counts.keys() else progress_counts[len_t]
