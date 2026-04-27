
def count_longest_valid_length(string: str) -> int:  # LeetCode Q.32.
    isolate_indices: list[int] = []  # Stack for indices of unpaired left parentheses.
    completions: list[list[int]] = []  # Format: [start idx, end idx].

    max_len = 0
    for idx, parenthesis in enumerate(string):
        if parenthesis == ")":
            if not isolate_indices:  # Completions are stopped by an unpaired right parenthesis.
                completions.clear()
                continue

            pair_idx = isolate_indices.pop(-1)
            while completions and pair_idx < completions[-1][0] < completions[-1][1] < idx:
                completions.pop(-1)  # Merge current pair with past completions.

            if completions and completions[-1][1] + 1 == pair_idx:  # Extend to last completion.
                completions[-1][1] = idx

            else:  # Current pair becomes last completion.
                completions.append([pair_idx, idx])

            current_len = completions[-1][1] + 1 - completions[-1][0]
            if current_len > max_len:
                max_len = current_len
            continue

        isolate_indices.append(idx)

    return max_len
