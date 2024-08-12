
def find_max_equal_frequency(numbers: list[int]):  # LeetCode Q.1224.
    max_len = 0
    # Track each number's frequency and each frequency's appearances.
    nums_freqs, freqs_counts = dict(), dict()

    for idx, num in enumerate(numbers):
        if num not in nums_freqs.keys():
            nums_freqs.update({num: 0})
        nums_freqs[num] += 1

        current_freq = nums_freqs[num]
        if current_freq not in freqs_counts.keys():
            freqs_counts.update({current_freq: 0})
        freqs_counts[current_freq] += 1

        if current_freq > 1:  # Need to update old frequency's count.
            freqs_counts[current_freq - 1] -= 1
            if freqs_counts[current_freq - 1] == 0:
                del freqs_counts[current_freq - 1]

        if len(freqs_counts) == 1:
            # Each number occurs once, or a number occurs every time.
            if 1 in freqs_counts.keys() or 1 in freqs_counts.values():
                max_len = idx + 1

        if len(freqs_counts) == 2:
            # A number occurs once while others has the same frequency.
            if 1 in freqs_counts.keys() and freqs_counts[1] == 1:
                max_len = idx + 1
                continue

            max_freq, min_freq = max(freqs_counts.keys()), min(freqs_counts.keys())
            # Higher frequency can merge into lower freqeuency.
            if freqs_counts[max_freq] == 1 and max_freq - min_freq == 1:
                max_len = idx + 1

    return max_len
