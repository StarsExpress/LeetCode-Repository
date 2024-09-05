
def _detect_duplicate(
    string: str, length: int, window_size: int, base: int = 31, mod: int = 2 ** 34 - 1
):
    powers = [1] + [0] * length  # 1st power starts from 1.
    hash_values = set()

    for i in range(1, length + 1):  # Precompute powers of base, and modulo over mod.
        powers[i] += (powers[i - 1] * base) % mod

    window_hash = 0
    for i in range(window_size):  # Hash value of 1st window.
        window_hash *= base
        window_hash += ord(string[i])
        window_hash %= mod
    hash_values.add(window_hash)

    for i in range(1, length - window_size + 1):  # Hash values of the rest windows.
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
    string_len = len(string)

    min_window, max_window = 1, string_len - 1  # Search space.
    while min_window <= max_window:  # Must include the case min window = max window.
        mid_window = (min_window + max_window) // 2
        duplicate_substring = _detect_duplicate(string, string_len, mid_window)
        if duplicate_substring:  # Can try a bigger window.
            longest_duplicate_substring = duplicate_substring
            min_window = mid_window + 1
            continue
        max_window = mid_window - 1  # Must try a smaller window.

    return longest_duplicate_substring
