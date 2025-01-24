import math


def count_divisible_pairs(numbers: list[int], k: int) -> int:  # LeetCode Q.2183.
    total_numbers = len(numbers)
    if k == 1:
        return total_numbers * (total_numbers - 1) // 2

    for integer in range(2, int(math.sqrt(k)) + 1):
        if k % integer == 0:  # k isn't a prime.
            break

    else:  # k is a prime.
        k_products, nums2products = 0, dict()
        for number in numbers:
            if number not in nums2products.keys():
                nums2products.update({number: 0})
                if number % k == 0:  # Value is 1 if number is divisible by k.
                    nums2products[number] += 1
            k_products += nums2products[number]

        return (k_products * (k_products - 1) // 2) + k_products * (total_numbers - k_products)

    distinct_numbers, max_number = [], -float("inf")
    numbers2counts, numbers2complements = dict(), dict()
    for number in numbers:
        if number not in numbers2counts.keys():
            if number > max_number:
                max_number = number

            distinct_numbers.append(number)
            numbers2complements.update({number: k // math.gcd(k, number)})
            numbers2counts.update({number: 0})
        numbers2counts[number] += 1

    pairs = 0
    for number in distinct_numbers:
        count = 0
        complement, multiplier = numbers2complements[number], 1
        if numbers2complements[number] < number:  # Enlarge complement so that it >= number.
            multiplier = number // numbers2complements[number]
            if number % numbers2complements[number] > 0:
                multiplier += 1
            complement = numbers2complements[number] * multiplier

        rounds = 1 + max_number // numbers2complements[number] - multiplier
        for _ in range(rounds):
            if complement in numbers2counts.keys():
                if complement == number:
                    pairs += numbers2counts[number] * (numbers2counts[number] - 1) // 2

                else:
                    count += numbers2counts[complement]

            complement += numbers2complements[number]

        pairs += numbers2counts[number] * count

    return pairs
