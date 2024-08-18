
def _detect_duplicate(string: str, window_size: int, base: int = 31, mod: int = 2 ** 34 - 1):
    str_len = len(string)
    powers = [1] + [0] * str_len  # 1st power starts from 1.
    hash_values = set()

    for i in range(1, str_len + 1):  # Precompute powers of base, and modulo over mod.
        powers[i] += (powers[i - 1] * base) % mod

    window_hash = 0
    for i in range(window_size):  # Hash value of 1st window.
        window_hash *= base
        window_hash += ord(string[i])
        window_hash %= mod
    hash_values.add(window_hash)

    for i in range(1, str_len - window_size + 1):  # Hash values of the rest windows.
        # Remove contribution of window's 1st char.
        window_hash -= powers[window_size - 1] * ord(string[i - 1])
        window_hash %= mod

        window_hash *= base  # Shift window by one char and add new char to hash.
        window_hash += ord(string[i + window_size - 1])
        window_hash %= mod

        if window_hash in hash_values:  # Duplicate detected.
            return string[i: i + window_size]
        hash_values.add(window_hash)

    return None  # No duplicates found.


def find_longest_duplicate(string: str):  # LeetCode Q.1044.
    longest_duplicate_substring = ""
    min_len, max_len = 1, len(string) - 1  # Min & max possible lengths if duplicate exists.
    while min_len <= max_len:  # While must include the case min len = max len.
        mid_len = (min_len + max_len) // 2

        duplicate_substring = _detect_duplicate(string, mid_len)
        if duplicate_substring:  # Can try a longer length.
            longest_duplicate_substring = duplicate_substring
            min_len = mid_len + 1
            continue
        max_len = mid_len - 1  # Must try a shorter length.

    return longest_duplicate_substring
