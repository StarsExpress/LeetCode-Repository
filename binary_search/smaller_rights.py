
def count_smaller_rights(integers: list[int]) -> list[int]:  # LeetCode Q.315.
    smaller_rights = []
    sorted_integers, count = [], 0  # Count of sorted integers.

    for integer in integers[::-1]:  # Iteration: from rightmost to leftmost.
        back_idx, front_idx = 0, count - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if sorted_integers[mid_idx] < integer:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        smaller_rights.append(back_idx)  # Back idx: number of right side ints < current integer.
        sorted_integers.insert(back_idx, integer)  # Back idx implies insertion idx.
        count += 1

    return smaller_rights[::-1]  # Reverse to make order from leftmost to rightmost.
