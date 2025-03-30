import math


def replace_non_coprimes(nums: list[int]) -> list[int]:  # LeetCode Q.2197.
    replacements = [nums.pop(0)]
    for num in nums:
        gcd = math.gcd(replacements[-1], num)
        while replacements and gcd > 1:  # Keep replacing previous replacements.
            num *= replacements.pop(-1) // gcd
            if replacements:
                gcd = math.gcd(replacements[-1], num)

        replacements.append(num)

    return replacements
