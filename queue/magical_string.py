
def count_ones_in_magical_string(length: int) -> int:  # LeetCode Q.481.
    first_19_chars, last_digit = "1221121221221121122", 2
    one_occurrences = 0
    for i in range(19):
        if i == length:
            return one_occurrences

        if first_19_chars[i] == "1":
            one_occurrences += 1

    owed_digits = [1, 1, 2, 1, 1, 2, 2]
    length -= 19
    while length > 0:
        if last_digit == 1:
            last_digit += 1  # Last digit: from 1 to 2.
            owed_digits.extend([2] * owed_digits[0])

        else:
            last_digit -= 1  # Last digit: from 2 to 1.
            owed_digits.extend([1] * owed_digits[0])
            one_occurrences += min(length, owed_digits[0])  # Can't exceed remaining length.

        length -= owed_digits.pop(0)

    return one_occurrences
