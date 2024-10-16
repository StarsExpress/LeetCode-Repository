
def _binary_search(target: tuple[int, int], monotonic_stack: list[tuple[int, int]]) -> int:
    if not monotonic_stack:
        return 0

    back_idx, front_idx = 0, len(monotonic_stack) - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if monotonic_stack[mid_idx] > target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of stack tuples > target, implying insertion idx.


def find_second_greater(numbers: list[int]) -> list[int]:  # LeetCode Q.2454.
    total_nums = len(numbers)
    second_greater = [-1] * total_nums
    stack_1: list[tuple[int, int]] = [(numbers[0], 0)]  # Decreasing monotonic stack: (num, idx).
    stack_2: list[tuple[int, int]] = []  # Decreasing monotonic stack: (num, idx).

    for current_idx in range(1, total_nums):
        while stack_2 and stack_2[-1][0] < numbers[current_idx]:
            _, past_idx = stack_2.pop(-1)
            second_greater[past_idx] = numbers[current_idx]

        while stack_1 and stack_1[-1][0] < numbers[current_idx]:
            # Use binary sort to ensure 2nd stack is decreasing.
            insertion_idx = _binary_search(stack_1[-1], stack_2)
            stack_2.insert(insertion_idx, stack_1.pop(-1))

        stack_1.append((numbers[current_idx], current_idx))

    return second_greater
