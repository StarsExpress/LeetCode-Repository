
def find_single_item(items: list[int | float | str]):
    xor_value = 0   # Exclusive or between 0 and any other value is value itself.
    for item in items:
        xor_value ^= item
    return xor_value


if __name__ == '__main__':
    print(find_single_item([4, 1, 2, 1, 2]))
