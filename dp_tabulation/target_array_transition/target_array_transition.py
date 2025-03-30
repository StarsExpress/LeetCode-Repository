
def calculate_min_transition(nums: list[int], targets: list[int]) -> int:  # LeetCode Q.3229.
    for idx in range(len(nums)):
        nums[idx] = targets[idx] - nums[idx]

    operations = 0
    positive_coverage, negative_coverage = 0, 0
    for num in nums:
        if 0 <= num:  # Need increments to reach target.
            negative_coverage = 0

            if positive_coverage < num:  # Need operations for extra coverage.
                operations += num - positive_coverage
            positive_coverage = num

        else:  # Need decrements to reach target.
            positive_coverage = 0

            if num < negative_coverage:  # Need operations for extra coverage.
                operations += negative_coverage - num
            negative_coverage = num

    return operations
