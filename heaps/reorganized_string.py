import heapq


def reorganize_string(string: str) -> str:  # LeetCode Q.767.
    """Always choose top two frequent letters to interchange."""
    counts_table = dict()
    for char in list(string):
        if char not in counts_table.keys():
            counts_table.update({char: 0})
        counts_table[char] += 1

    max_heap = []
    for char, count in counts_table.items():
        heapq.heappush(max_heap, (-count, char))  # Negate count to fit max heap.

    rearranged_chars = ""
    queue = []  # Element format: (count, char).
    while max_heap:
        while len(queue) < 2 and max_heap:  # Fill queue.
            count, char = heapq.heappop(max_heap)
            queue.append([-count, char])  # Negate count back to positive int.

        if len(queue) < 2:
            break

        if max_heap:  # Threshold is max heap's max remaining count.
            threshold = -max_heap[0][0]  # Negate count back to positive int.

        else:
            threshold = 1

        while queue[1][0] >= threshold:
            rearranged_chars += f"{queue[0][1]}{queue[1][1]}"
            queue[0][0] -= 1
            queue[1][0] -= 1

        for _ in range(2):  # Clear queue.
            if threshold > queue[-1][0]:
                if queue[-1][0] > 0:  # Need to go back to max heap.
                    # Negate count to fit max heap.
                    heapq.heappush(max_heap, (-queue[-1][0], queue[-1][1]))

                queue.pop(-1)

    if queue:  # A type of char remains.
        if queue[0][0] > 1:
            return ""
        rearranged_chars += queue[0][1]

    return rearranged_chars
