
def compute_rolling_hash(string: str, window_size: int, base: int = 31, mod: int = 2 ** 31 - 1):
    """
    Calculate rolling hash values of all substrings of length window size in input string.
    Use polynomial rolling hash algorithm with base and mod as constants.
    """
    str_len = len(string)
    powers = [1] + [0] * str_len  # 1st power starts from 1.
    hash_values = [0] * (str_len - window_size + 1)

    for i in range(1, str_len + 1):  # Precompute powers of base, and modulo over mod.
        powers[i] += (powers[i - 1] * base) % mod

    window_hash = 0
    for i in range(window_size):  # Hash value of 1st window.
        window_hash *= base
        window_hash += ord(string[i])
        window_hash %= mod
    hash_values[0] += window_hash

    for i in range(1, str_len - window_size + 1):  # Hash values of the rest windows.
        # Remove contribution of window's 1st char.
        window_hash -= powers[window_size - 1] * ord(string[i - 1])
        window_hash %= mod

        window_hash *= base  # Shift window by one char and add new char to hash.
        window_hash += ord(string[i + window_size - 1])
        window_hash %= mod
        hash_values[i] += window_hash

    return hash_values
