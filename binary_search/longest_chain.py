
def create_longest_chain(pairs: list[list[int]]) -> int:  # LeetCode Q.646.
    pairs.sort(key=lambda x: (x[0], -x[1]))
    chain, length = [], 0  # Chain length.

    for left_num, right_num in pairs:
        back_idx, front_idx = 0, length - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if chain[mid_idx] < right_num:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        if back_idx == length:  # After binary search is over, back idx is insertion idx.
            if not (chain and left_num <= chain[-1]):  # Left num must > chain's last num.
                chain.append(right_num)
                length += 1
            continue

        chain[back_idx] = right_num

    return length
