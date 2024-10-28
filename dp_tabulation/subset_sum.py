
def find_constrained_subset_sum(numbers: list[int], k: int) -> int:  # LeetCode Q.1425.
    # Base case: subsequence of only 1st number.
    best_sum = [numbers[0]] + [0] * (len(numbers) - 1)
    max_sum = numbers[0]

    # Queue contains indices of best sums from current idx - k to current idx - 1.
    idx_queue = [0]  # Queue's 1st idx always points to window's best sum.
    for idx, number in enumerate(numbers):
        if idx == 0:  # Base case is already done.
            continue

        best_sum[idx] = number + max(best_sum[idx_queue[0]], 0)
        if best_sum[idx] > max_sum:
            max_sum = best_sum[idx]

        # Ensure last idx's corresponding best sum > current number's best sum.
        while idx_queue and best_sum[idx_queue[-1]] <= best_sum[idx]:
            idx_queue.pop(-1)

        # Ensure 1st idx will be in "next iteration's window".
        while idx_queue and idx_queue[0] < idx - k + 1:
            idx_queue.pop(0)

        idx_queue.append(idx)

    return max_sum
