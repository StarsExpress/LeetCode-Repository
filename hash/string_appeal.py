
def sum_total_appeal(string: str) -> int:  # LeetCode 2262.
    """
    Number of substrings ending at ith idx that contain a specific char
    = 1 + the last occurrence idx of the char before (i + 1)th idx.

    Total appeal of all substrings ending at ith idx
    = sum of number of substrings containing each character.
    """
    total_appeal, last_appeal = 0, 0
    chars_inclusions = dict()  # Number of substrings containing each char.
    for idx, char in enumerate(string):
        if char in chars_inclusions.keys():
            last_appeal -= chars_inclusions[char]
        last_appeal += 1 + idx

        total_appeal += last_appeal
        chars_inclusions.update({char: 1 + idx})

    return total_appeal
