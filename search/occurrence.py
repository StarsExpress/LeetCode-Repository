
def search_occurrence(nums_list: list[int], target: int):
    if target not in nums_list:
        return [-1, -1]

    start = nums_list.index(target)
    nums_list.reverse()
    return [start, len(nums_list) - nums_list.index(target) - 1]
