
def find_max_erasure(integers: list[int]):
    if len(integers) <= 0:
        return 0

    ints_list, idx_list = [integers[0]], [0]  # The same index means an int and its idx.

    current_erasure, max_erasure = integers[0], integers[0]  # Current subset has 1st int, so erasure = 1st int.
    current_idx, locator_idx = 1, 0  # Locator index helps update lists of subset ints and idx.

    while True:
        if current_idx >= len(integers):  # Reach the end of input list.
            return max(current_erasure, max_erasure)

        if integers[current_idx] not in ints_list:  # Current int isn't in current subset.
            ints_list.append(integers[current_idx])
            idx_list.append(current_idx)
            current_erasure += integers[current_idx]

        else:  # Current int is already in "somewhere" of current subset.
            max_erasure += max(current_erasure - max_erasure, 0)  # Update max erasure.

            # Locate where this current int is at ints & idx list.
            locator_idx += ints_list.index(integers[current_idx]) - locator_idx
            # Ensure uniqueness in current subset, and adjust its erasure.
            current_erasure -= sum(ints_list[: locator_idx + 1]) - integers[current_idx]

            ints_list = ints_list[locator_idx + 1:]  # Update ints and idx list.
            ints_list.append(integers[current_idx])
            idx_list = idx_list[locator_idx + 1:]
            idx_list.append(current_idx)

        current_idx += 1  # Go to next int of input list.


if __name__ == '__main__':
    numbers = [4, 2, 4, 5, 6]
    print(find_max_erasure(numbers))
