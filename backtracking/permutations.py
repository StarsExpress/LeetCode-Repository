
def collect_permutations(nums: list[int]) -> list[list[int]]:  # LeetCode Q.46.
    permutations: list[list[int]] = [[]]
    permutation_len, intermediates = 0, []
    for num in nums:
        for permutation in permutations:
            for insertion_idx in range(permutation_len + 1):
                intermediate = permutation.copy()
                intermediate.insert(insertion_idx, num)
                intermediates.append(intermediate)

        permutations.clear()
        permutations.extend(intermediates)
        permutation_len += 1
        intermediates.clear()

    return permutations
