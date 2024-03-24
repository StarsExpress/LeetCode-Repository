
def find_duplicate_item(items: list[int | float | str]):  # Leetcode Q.287.
    items.sort()
    for i in range(len(items) - 1):
        if items[i] == items[i + 1]:
            return items[i]
    return None


def search_missed_int(ints: list[int]):  # Leetcode Q.645: desired integers are 1 to n, but one is misplaced by another.
    ints.sort()
    missed_int = (set(range(1, len(ints) + 1)) - set(ints)).pop()
    for i in range(len(ints) - 1):
        if ints[i] == ints[i + 1]:
            return [ints[i], missed_int]


if __name__ == '__main__':
    print(search_missed_int([1, 3, 4, 2, 2]))
