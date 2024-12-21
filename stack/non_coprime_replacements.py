import math


def replace_non_coprimes(numbers: list[int]) -> list[int]:  # LeetCode Q.2197.
    replacements = [numbers.pop(0)]
    for number in numbers:
        gcd = math.gcd(replacements[-1], number)
        while replacements and gcd > 1:  # Keep replacing previous replacements.
            number *= replacements.pop(-1) // gcd
            if replacements:
                gcd = math.gcd(replacements[-1], number)

        replacements.append(number)

    return replacements
