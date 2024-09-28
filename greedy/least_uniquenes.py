
def find_least_unique_ints(numbers: list[int], k: int) -> int:  # LeetCode Q.1481.
    """Find the least number of unique integers after removal of k integers."""
    total_unique_nums = 0
    # Occurrences list: idx + 1 = occurrence, value = count of numbers with that occurrence.
    nums2occurrences, occurrences, occurrences_len = dict(), [], 0
    for number in numbers:
        if number not in nums2occurrences.keys():
            total_unique_nums += 1
            nums2occurrences.update({number: 0})
        nums2occurrences[number] += 1

        if nums2occurrences[number] >= 2:  # Decrement count of old occurrence.
            occurrences[nums2occurrences[number] - 2] -= 1

        if nums2occurrences[number] > occurrences_len:
            occurrences.append(1)
            occurrences_len += 1

        else:
            occurrences[nums2occurrences[number] - 1] += 1

    while k >= 0:
        for occurrence, count in enumerate(occurrences):
            occurrence += 1
            total_unique_nums -= min(count, k // occurrence)

            k -= occurrence * count
            if k < 0:
                return total_unique_nums
