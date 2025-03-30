
def calculate_min_formation(target: list[int]) -> int:  # LeetCode Q.1526.
    coverage, operations = 0, 0
    for num in target:
        if coverage < num:  # Need operations for additional coverage.
            operations += num - coverage
        coverage = num

    return operations
