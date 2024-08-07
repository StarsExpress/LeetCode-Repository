
def find_combination_sum(nums: list[int], target: int):  # LeetCode Q.377.
    # Base case: 0 target has only 1 permutation (no numbers at all).
    permutations = [1] + [0] * target
    for iter_target in range(1, target + 1):
        for num in nums:
            if iter_target < num:  # Current num can't build up target.
                continue

            # Directly sum up to reflect all "permutations".
            permutations[iter_target] += permutations[iter_target - num]

    return permutations[target]
