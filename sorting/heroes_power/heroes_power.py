
def sum_heroes_power(nums: list[int]) -> int:  # LeetCode Q.2681.
    nums.sort()

    heroes_power_sum, modulo = 0, 10 ** 9 + 7
    prefix_sum = 0
    for num in nums:
        heroes_power_sum += (prefix_sum + num) * (num ** 2)
        heroes_power_sum %= modulo
        prefix_sum *= 2
        prefix_sum += num
        prefix_sum %= modulo

    return heroes_power_sum
