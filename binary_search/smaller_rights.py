
def count_smaller_rights(integers: list[int]) -> list[int]:  # LeetCode Q.315.
    smaller_rights = []
    sorted_integers, count = [], 0  # Count of sorted integers.

    for integer in integers[::-1]:  # Iteration: from rightmost to leftmost.
        left_idx, right_idx = 0, count - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if sorted_integers[mid_idx] < integer:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        smaller_rights.append(left_idx)  # Back idx: number of right side ints < current integer.
        sorted_integers.insert(left_idx, integer)  # Back idx implies insertion idx.
        count += 1

    return smaller_rights[::-1]  # Reverse to make order from leftmost to rightmost.
