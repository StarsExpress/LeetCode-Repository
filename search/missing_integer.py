
def find_1st_missing_positive(nums: list[int]) -> int:
    unique_nums = set(nums)
    unique_positives = set(range(1, len(unique_nums) + 1))  # From 1 to unique numbers count.
    unique_positives -= unique_positives & unique_nums  # The "remaining" positives.
    if len(unique_positives) <= 0:  # When inputs are "unique & consecutive positives" that wipe away everything.
        return len(unique_nums) + 1
    return min(unique_positives)


if __name__ == '__main__':
    print(find_1st_missing_positive([3, 4, 2, 1]))
