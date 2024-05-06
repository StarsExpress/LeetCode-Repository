
def binary_search(target: int, sorted_integers: list[int] | tuple[int]):
    if len(sorted_integers) <= 0:
        return 0

    back_idx, front_idx = 0, len(sorted_integers) - 1
    while True:
        if back_idx > front_idx:
            return back_idx  # Number of ints < target.

        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1


def find_longest_rising_subsequence(numbers: list[int]):  # LeetCode Q.300.
    subsequence = []
    while numbers:
        newcomer = numbers.pop(0)
        insertion_idx = binary_search(newcomer, subsequence)
        if insertion_idx == len(subsequence):
            subsequence.append(newcomer)
            continue
        subsequence[insertion_idx] = newcomer

    return len(subsequence)
