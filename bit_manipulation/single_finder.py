
def find_single_integer(integers: list[int]) -> int:  # LeetCode 136.
    """One int appears once while others appear twice. Find this int."""
    xor_value = integers.pop(0)
    while integers:
        xor_value ^= integers.pop(0)
    return xor_value
