
def create_longest_chain(pairs: list[list[int]]) -> int:  # LeetCode Q.646.
    pairs.sort(key=lambda x: (x[0], -x[1]))
    chain, length = [], 0  # Chain length.

    for left_num, right_num in pairs:
        left_idx, right_idx = 0, length - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if chain[mid_idx] < right_num:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        if left_idx == length:  # After binary search is over, back idx is insertion idx.
            if not (chain and left_num <= chain[-1]):  # Left num must > chain's last num.
                chain.append(right_num)
                length += 1
            continue

        chain[left_idx] = right_num

    return length
