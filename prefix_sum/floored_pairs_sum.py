
def calculate_floored_pairs_sum(nums: list[int]):  # LeetCode Q.1862.
    max_num = max(nums)
    frequencies = [0] * (max_num + 1)
    for num in nums:
        frequencies[num] += 1

    freqs_prefix_sums = []
    for frequency in frequencies:
        if not freqs_prefix_sums:
            freqs_prefix_sums.append(frequency)
            continue
        freqs_prefix_sums.append(freqs_prefix_sums[-1] + frequency)

    total_sum, unique_nums = 0, set(nums)
    for num in unique_nums:
        for multiple in range(1, max_num // num + 1):
            # Frequencies from multiple * num to the smaller of (multiple + 1) * num - 1 and max num.
            total_frequencies = freqs_prefix_sums[min((multiple + 1) * num - 1, max_num)]
            total_frequencies -= freqs_prefix_sums[multiple * num - 1]
            total_sum += multiple * frequencies[num] * total_frequencies

    return total_sum % (10 ** 9 + 7)  # Required to control sum size.
