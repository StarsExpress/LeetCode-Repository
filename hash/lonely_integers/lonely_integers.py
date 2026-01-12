
def find_lonely_integers(nums: list[int]) -> list[int]:  # LeetCode Q.2150.
    nums2counts: dict[int, int] = dict()
    for num in nums:
        if num not in nums2counts.keys():
            nums2counts.update({num: 0})
        nums2counts[num] += 1
    
    lonely_nums = []
    for num in nums:
        if nums2counts[num] == 1:
            if num - 1 not in nums2counts.keys():
                if num + 1 not in nums2counts.keys():
                    lonely_nums.append(num)
    
    return lonely_nums
