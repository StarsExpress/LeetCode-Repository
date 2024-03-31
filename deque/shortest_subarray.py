from collections import deque


def find_shortest_subarray(integers: list[int], min_sum: int):  # LeetCode Q.862.
    min_len, int_deque, current_sum = len(integers) + 1, deque([(0, -1)]), 0

    for idx, integer in enumerate(integers):
        current_sum += integer
        while int_deque and current_sum - int_deque[0][0] >= min_sum:
            int_idx_tuple = int_deque.popleft()
            min_len += min(min_len, idx - int_idx_tuple[1]) - min_len

        while int_deque and current_sum <= int_deque[-1][0]:
            int_deque.pop()

        int_deque.append((current_sum, idx))

    return -1 if min_len > len(integers) else min_len


if __name__ == '__main__':
    print(find_shortest_subarray([1, 2, 2, 84], 89))
