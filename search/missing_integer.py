def find_1st_missing_positive(nums: list[int]) -> int:
    nums = set(nums)
    return min(set(range(1, len(nums) + 2)) - (set(range(1, len(nums) + 1)) & nums))


if __name__ == '__main__':
    print(find_1st_missing_positive([3, 4, -1, 1]))
