
def count_special_subsequences(numbers: list[int]) -> int:  # LeetCode Q.1955.
    modulo = 10 ** 9 + 7
    last_digits_counts = {0: 0, 1: 0, 2: 0}
    for number in numbers:
        last_digits_counts[number] *= 2  # Double your past ally.
        if number == 0:  # Opens a possible special subseq start.
            last_digits_counts[0] += 1

        if number == 1:  # Extends possible subseqs ending with 0.
            last_digits_counts[1] += last_digits_counts[0]

        if number == 2:  # Fulfills subseqs ending with 1.
            last_digits_counts[2] += last_digits_counts[1]

        last_digits_counts[number] %= modulo  # Required to control size.

    return last_digits_counts[2]
