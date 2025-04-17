
def calculate_min_transition(nums: list[int], targets: list[int]) -> int:  # LeetCode Q.3229.
    operations = 0
    positive_coverage, negative_coverage = 0, 0
    for idx, target in enumerate(targets):
        target -= nums[idx]
        if 0 <= target:  # Need increments to reach target.
            negative_coverage = 0

            # Operations for extra coverage.
            operations += max(target - positive_coverage, 0)
            positive_coverage = target

        else:  # Need decrements to reach target.
            positive_coverage = 0

            # Operations for extra coverage.
            operations += max(negative_coverage - target, 0)
            negative_coverage = target

    return operations
