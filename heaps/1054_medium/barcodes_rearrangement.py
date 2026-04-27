import heapq


def rearrange_barcodes(barcodes: list[int]) -> list[int]:  # LeetCode Q.1054.
    """Always choose the most common two barcodes to interchange."""
    counts_table = dict()
    for barcode in barcodes:
        if barcode not in counts_table.keys():
            counts_table.update({barcode: 0})
        counts_table[barcode] += 1

    max_heap = []
    for barcode, count in counts_table.items():
        heapq.heappush(max_heap, (-count, barcode))  # Negate count to fit max heap.

    rearranged_barcodes = []
    queue = []  # Element format: (count, barcode).
    while max_heap:
        while len(queue) < 2 and max_heap:  # Fill queue.
            count, barcode = heapq.heappop(max_heap)
            queue.append([-count, barcode])  # Negate count back to positive int.

        if len(queue) < 2:
            break

        if max_heap:  # Threshold is max heap's max remaining count.
            threshold = -max_heap[0][0]  # Negate count back to positive int.

        else:
            threshold = 1

        while queue[1][0] >= threshold:
            rearranged_barcodes.extend([queue[0][1], queue[1][1]])
            queue[0][0] -= 1
            queue[1][0] -= 1

        for _ in range(2):  # Clear queue.
            if threshold > queue[-1][0]:
                if queue[-1][0] > 0:  # Need to go back to max heap.
                    # Negate count to fit max heap.
                    heapq.heappush(max_heap, (-queue[-1][0], queue[-1][1]))

                queue.pop(-1)

    if queue:  # A type of barcode remains.
        rearranged_barcodes.append(queue[0][1])
    return rearranged_barcodes
