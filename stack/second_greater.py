
def _binary_search(target: tuple[int, int], monotonic_stack: list[tuple[int, int]]):
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


def find_second_greater(numbers: list[int]):  # LeetCode Q.2454.
    second_greater = [-1] * len(numbers)
    stack_1, stack_2 = [(numbers[0], 0)], []  # Decreasing monotonic stacks: (num, idx).

    for current_idx in range(1, len(numbers)):
        if stack_2:
            past_num, past_idx = stack_2.pop(-1)
            while past_num < numbers[current_idx]:
                second_greater[past_idx] = numbers[current_idx]
                if not stack_2:
                    break
                past_num, past_idx = stack_2.pop(-1)

            if past_num >= numbers[current_idx]:
                stack_2.append((past_num, past_idx))

        if stack_1:
            past_num, past_idx = stack_1.pop(-1)
            while past_num < numbers[current_idx]:
                # Use binary sort to ensure 2nd stack is decreasing.
                insertion_idx = _binary_search((past_num, past_idx), stack_2)
                stack_2.insert(insertion_idx, (past_num, past_idx))
                if not stack_1:
                    break
                past_num, past_idx = stack_1.pop(-1)

            if past_num >= numbers[current_idx]:
                stack_1.append((past_num, past_idx))

        stack_1.append((numbers[current_idx], current_idx))

    return second_greater
