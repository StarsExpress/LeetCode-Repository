
def count_k_inverse_pairs_arrays(n: int, k: int) -> int:  # LeetCode Q.629.
    if k == 0:  # Base case: k = 0.
        return 1
    if k > n * (n - 1) // 2:  # Base case: k > different pairs count.
        return 0

    inverse_counts = [[1] * (k + 1), [1] * (k + 1)]  # Cumulated counts.
    for num in range(2, n + 1):
        max_inverse = min(k, num * (num - 1) // 2)
        for inverse in range(1, k + 1):  # 0 inverse keeps count of 1.
            inverse_counts[1][inverse] = inverse_counts[1][inverse - 1]
            if inverse <= max_inverse:
                inverse_counts[1][inverse] += inverse_counts[0][inverse]
                if inverse - num >= 0:  # Window size = num.
                    inverse_counts[1][inverse] -= inverse_counts[0][inverse - num]

        inverse_counts[0][:] = inverse_counts[1][:]  # Must use [:] to update array.

    # Required to control size.
    return (inverse_counts[1][k] - inverse_counts[1][k - 1]) % (10 ** 9 + 7)
