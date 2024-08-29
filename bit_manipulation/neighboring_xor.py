
def verify_array_existence(derived: list[int]):  # LeetCode Q.2683.
    xor_value = derived.pop(0)
    for derive in derived:
        xor_value ^= derive
    return xor_value == 0
