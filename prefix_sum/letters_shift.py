import string


def shift_letters(letters: str, shifts: list[int]) -> str:  # LeetCode Q.848.
    lower_cases = list(string.ascii_lowercase)
    chars2ints = dict(zip(lower_cases, [i for i in range(26)]))

    integers = [chars2ints[char] for char in list(letters[::-1])]  # Reverse chars.
    prefix_sum = 0
    for idx, shift in enumerate(shifts[::-1]):  # Reverse iteration of shifts.
        prefix_sum += shift
        integers[idx] += prefix_sum
        integers[idx] %= 26

    return "".join(lower_cases[integer] for integer in integers[::-1])  # Back to original order.
