
def _rolling_hash(
    nums: list[int], total_nums: int, window_size: int, base: int = 101, mod: int = 2 ** 26 - 1,
):
    powers = [1] + [0] * total_nums  # 1st power starts from 1.
    hash_values = set()

    for i in range(
        1, total_nums + 1
    ):  # Precompute powers of base, and modulo over mod.
        powers[i] += (powers[i - 1] * base) % mod

    window_hash = 0
    for i in range(window_size):  # Hash value of 1st window.
        window_hash *= base
        window_hash += nums[i]
        window_hash %= mod
    hash_values.add(window_hash)

    for i in range(1, total_nums - window_size + 1):  # Hash values of the rest windows.
        # Remove contribution of window's 1st char.
        window_hash -= powers[window_size - 1] * nums[i - 1]
        window_hash %= mod

        window_hash *= base  # Shift window by one char and add new char to hash.
        window_hash += nums[i + window_size - 1]
        window_hash %= mod
        hash_values.add(window_hash)

    return hash_values


def find_longest_length(numbers_1: list[int], numbers_2: list[int]):  # LeetCode Q.718.
    if set(numbers_1) & set(numbers_2) == set():  # Base case.
        return 0

    longest_length = 1  # Now length is at least 1.
    numbers_1_len, numbers_2_len = len(numbers_1), len(numbers_2)

    min_len, max_len = 2, min(numbers_1_len, numbers_2_len)  # Search space.
    while min_len <= max_len:  # While must include the case min len = max len.
        mid_len = (min_len + max_len) // 2
        common_hash_values = _rolling_hash(
            numbers_1, numbers_1_len, mid_len
        ) & _rolling_hash(numbers_2, numbers_2_len, mid_len)

        if common_hash_values != set():  # Can try a longer length.
            longest_length = mid_len
            min_len = mid_len + 1
            continue
        max_len = mid_len - 1  # Must try a shorter length.

    return longest_length
