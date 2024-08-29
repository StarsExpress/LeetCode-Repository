
def sum_integers(a: int, b: int):  # LeetCode Q.371.
    if max(a, b) < 0:
        double_negatives = True
        a, b = abs(a), abs(b)

    else:
        double_negatives = False

    integers_sum = 2 * (a & b)  # AND: common digits getting doubled.
    integers_sum += a ^ b  # XOR: differed digits between a and b.
    return -integers_sum if double_negatives else integers_sum
