
def count_unique_digits(power: int):  # LeetCode Q.357.
    # Given power, return count of all numbers x that satisfy 0 <= x < 10 ** power and have unique digits.
    if power <= 0:
        return 1
    if power == 1:
        return 10

    # If n >= 2: know the count "up to" last power (power = n - 1).
    last_power_count = count_unique_digits(power - 1)

    # Find the count "right at" current power (power = n).
    current_power_count = 9  # Current power >= 2: leading digit's choice = 9 (0 excluded).
    for i in range(2, power + 1):
        if i == 2:  # 2nd leftmost digit's choice = 9 - 1 + 1 (0 can come in).
            current_power_count *= 9
            continue
        current_power_count *= (10 - i + 1)  # From 3rd leftmost digit, choice = 8, 7, ..., etc.
    return last_power_count + current_power_count  # Count "up to" current power.
