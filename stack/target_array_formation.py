
def calculate_min_formation(target: list[int]) -> int:  # LeetCode Q.1526.
    min_operations = 0
    # Cushion: head number's left neighbor target array. Default to 0.
    head, cushion = 0, 0
    for idx, number in enumerate(target):
        if idx == 0:
            head = number

        if idx > 0 and number > target[idx - 1]:
            min_operations += head - cushion
            head, cushion = number, target[idx - 1]

    return min_operations + head - cushion  # Deal with the last iteration.
