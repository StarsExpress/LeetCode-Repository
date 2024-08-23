
def count_subarrays(numbers: list[int]):  # LeetCode Q.1524.
    odd_subarrays_count = 0
    prefix_sum, odd_count = 0, 0
    for idx, num in enumerate(numbers):
        prefix_sum += num  # Update current prefix sum.
        if prefix_sum % 2 == 0:  # Even current prefix sum: take odd count.
            odd_subarrays_count += odd_count
            continue

        # Odd current prefix sum: take even count.
        odd_subarrays_count += idx + 1 - odd_count
        odd_count += 1  # Update count: current prefix sum is odd.

    return odd_subarrays_count % (10 ** 9 + 7)
