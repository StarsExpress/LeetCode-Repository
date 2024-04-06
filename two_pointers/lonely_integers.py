
def find_lonely_integers(integers: list[int]):  # LeetCode Q.2150.
    if len(integers) <= 1:
        return integers

    integers.sort()
    lonely_nums, current_idx = [], 1
    if integers[0] + 1 < integers[1]:
        lonely_nums.append(integers[0])

    while True:
        if current_idx >= len(integers) - 1:
            if integers[current_idx - 1] + 1 < integers[current_idx]:
                lonely_nums.append(integers[current_idx])
            return lonely_nums

        if integers[current_idx - 1] + 1 < integers[current_idx]:
            if integers[current_idx] + 1 < integers[current_idx + 1]:
                lonely_nums.append(integers[current_idx])
        current_idx += 1
