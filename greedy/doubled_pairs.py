
def verify_doubled_pairs(array: list[int]) -> bool:  # LeetCode Q.954.
    negative_counts, positive_counts = dict(), dict()
    for number in array:
        if number < 0:
            if number not in negative_counts.keys():
                negative_counts.update({number: 0})
            negative_counts[number] += 1

        if number > 0:
            if number not in positive_counts.keys():
                positive_counts.update({number: 0})
            positive_counts[number] += 1

    negatives = sorted(negative_counts.keys())
    while negatives:
        negative = negatives.pop(-1)
        if negative in negative_counts.keys():
            double_negative = negative * 2
            if double_negative not in negative_counts.keys():  # Double doesn't exist.
                return False

            negative_counts[double_negative] -= negative_counts[negative]
            if negative_counts[double_negative] < 0:  # Can't cover.
                return False
            if negative_counts[double_negative] == 0:  # Depleted.
                del negative_counts[double_negative]

    positives = sorted(positive_counts.keys())
    while positives:
        positive = positives.pop(0)
        if positive in positive_counts.keys():
            double_positive = positive * 2
            if double_positive not in positive_counts.keys():  # Double doesn't exist.
                return False

            positive_counts[double_positive] -= positive_counts[positive]
            if positive_counts[double_positive] < 0:  # Can't cover.
                return False
            if positive_counts[double_positive] == 0:  # Depleted.
                del positive_counts[double_positive]

    return True
