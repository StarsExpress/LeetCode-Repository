
def search_occurrence(integers_list: list[int], target: int):
    if target not in integers_list:
        return [-1, -1]

    start = integers_list.index(target)
    integers_list.reverse()
    return [start, len(integers_list) - integers_list.index(target) - 1]
