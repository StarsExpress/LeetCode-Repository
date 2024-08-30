
def compute_all_pairings_xor(numbers_1: list[int], numbers_2: list[int]):  # LeetCode Q.2425.
    all_pairings_xor_value = 0
    if len(numbers_2) % 2 == 1:
        for num in numbers_1:
            all_pairings_xor_value ^= num

    if len(numbers_1) % 2 == 1:
        for num in numbers_2:
            all_pairings_xor_value ^= num

    return all_pairings_xor_value
