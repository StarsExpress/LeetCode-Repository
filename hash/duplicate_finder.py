
def find_duplicate_integer(nums: list[int]) -> int:  # LeetCode Q.287.
    """Only 1 int repeats while others each occur once. All ints are between 1 and len(nums) - 1."""
    duplicate = -1
    for num in nums:
        idx = abs(num)
        if nums[idx] < 0:
            duplicate = idx
            break
        nums[idx] = -nums[idx]

    return duplicate


def seek_missed_integer(nums: list[int]) -> list[int]:  # LeetCode Q.645.
    """
    Desired ints: 1 to n, but one is misplaced by another.
    """
    total_nums = len(nums)
    n_to_1_counts = dict(zip(range(1, total_nums + 1), [1] * total_nums))

    duplicate_and_missing = []  # Format: [duplicate num, missing num].
    for num in nums:
        if num not in n_to_1_counts.keys():
            duplicate_and_missing.append(num)

        else:
            del n_to_1_counts[num]

    duplicate_and_missing.append(list(n_to_1_counts.keys())[0])
    return duplicate_and_missing
