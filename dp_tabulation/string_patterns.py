
def count_unique_words(word_length: int, max_vowels_streak: int) -> int:
    if word_length <= 0: return 0  # Sanity check.

    # Indices: suffix vowels streak.
    # Values: num of unique words given current length and suffix vowels streak.
    counts_table: list[int] = [21]  # Base case at length of 1.
    if max_vowels_streak > 0: counts_table.append(5)

    modulo = 10 ** 9 + 7  # To prevent overflow.

    for _ in range(2, word_length + 1):
        new_counts_table = [0] * len(counts_table)
        # Case 1: add another consonant. Prevent overflow.
        new_counts_table[0] = (sum(counts_table) * 21) % modulo

        for vowels_streak, count in enumerate(counts_table):
            # Case 2: add a vowel. Check eligibility first.
            if vowels_streak + 1 <= max_vowels_streak:
                if vowels_streak + 1 >= len(new_counts_table):
                    new_counts_table.append(0)

                new_counts_table[vowels_streak + 1] += count * 5
                new_counts_table[vowels_streak + 1] %= modulo  # To prevent overflow.

        counts_table.clear()  # Reset before updates.
        counts_table.extend(new_counts_table)

    return sum(counts_table)


print(count_unique_words(4, 2))
