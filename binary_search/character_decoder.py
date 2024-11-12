
def decode_kth_index_character(string: str, k: int) -> str:  # LeetCode Q.880.
    decoded_len = 0
    indices, decoded_lens = [], []  # Map indices to respective decoded lengths.
    for idx, char in enumerate(string):
        if char.isdigit():
            decoded_len *= int(char)  # Extend the length.
            if decoded_len >= k:
                break

        else:  # Char isn't a digit.
            decoded_len += 1
            if decoded_len == k:  # Answer is found.
                return char

        indices.append(idx)
        decoded_lens.append(decoded_len)

    back_idx, front_idx = 0, len(decoded_lens) - 1  # Binary search for decoded char.
    target = k
    while front_idx >= 0:
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if decoded_lens[mid_idx] <= target:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        target %= decoded_lens[back_idx - 1]
        if target == 0:  # s[:indices[back_idx - 1] + 1] has the answer.
            for idx in range(indices[back_idx - 1], -1, -1):  # Backward iteration.
                if not string[idx].isdigit():  # Answer is the 1st found char.
                    return string[idx]

        back_idx, front_idx = 0, back_idx - 1
