
def find_longest_rising_subsequence(numbers: list[int]):  # LeetCode Q.300.
    rising_subsequence, subsequence_len = [], 0
    while numbers:
        newcomer = numbers.pop(0)
        # After binary search is over, back idx is insertion idx.
        back_idx, front_idx = 0, subsequence_len - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if rising_subsequence[mid_idx] < newcomer:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        if back_idx == subsequence_len:
            rising_subsequence.append(newcomer)
            subsequence_len += 1

        else:
            rising_subsequence[back_idx] = newcomer

    return subsequence_len
