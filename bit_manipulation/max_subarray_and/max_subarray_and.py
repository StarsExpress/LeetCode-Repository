
def find_longest_subarray(nums: list[int]) -> int:  # LeetCode Q.2419.
    longest_len = 1  # Base case.
    max_num, max_streak = 0, 0

    for num in nums:
        if num != max_num:
            max_streak -= max_streak  # Reset.
            if num > max_num: max_num, longest_len = num, 1  # Reset.
        
        if num == max_num:
            max_streak += 1
            if max_streak > longest_len: longest_len = max_streak
    
    return longest_len
