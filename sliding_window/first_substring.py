import string


def find_substring(input_str: str, power: int, modulo: int, k: int, hash_value: int) -> str:  # LeetCode Q.2156.
    chars2values = dict(zip(string.ascii_lowercase, range(1, 27)))

    window_chars, window_numerator = [input_str[0]], chars2values[input_str[0]]  # 1st char is in as k >= 1.
    rolling_power = 1
    for char in input_str[1:k]:
        window_chars.append(char)
        rolling_power *= power
        window_numerator += chars2values[char] * rolling_power

    if window_numerator % modulo == hash_value:
        return input_str[:k]

    for char in input_str[k:]:
        window_numerator -= chars2values[window_chars.pop(0)]
        window_numerator //= power

        window_chars.append(char)
        window_numerator += chars2values[char] * rolling_power

        if window_numerator % modulo == hash_value:
            return "".join(window_chars)
