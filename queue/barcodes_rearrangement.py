
def _binary_search(target: int, sorted_integers: list[int] | tuple[int]):
    if not sorted_integers:
        return 0

    back_idx, front_idx = 0, len(sorted_integers) - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] > target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints > target, implying insertion idx.


def rearrange_barcodes(barcodes: list[int]):  # LeetCode Q.1054.
    """Always choose the most common two barcodes to interchange."""
    if len(barcodes) == 1:  # Base case.
        return barcodes

    counts_table = dict()
    for barcode in barcodes:
        if barcode not in counts_table.keys():
            counts_table.update({barcode: 0})
        counts_table[barcode] += 1

    counts_table = dict(sorted(counts_table.items(), key=lambda item: item[1], reverse=True))
    barcodes_pool = list(counts_table.keys())
    counts_pool = list(counts_table.values())

    queue, rearranged_barcodes = [], []
    while barcodes_pool and counts_pool:
        while len(queue) < 2:  # Fill queue.
            queue.append([counts_pool.pop(0), barcodes_pool.pop(0)])

        threshold = counts_pool[0] if counts_pool else 1
        while queue[1][0] >= threshold:
            rearranged_barcodes.extend([queue[0][1], queue[1][1]])
            queue[0][0] -= 1
            queue[1][0] -= 1

        for _ in range(2):  # Clear queue.
            if counts_pool and counts_pool[0] > queue[-1][0]:
                if queue[-1][0] > 0:  # Need to insert back to pools.
                    insertion_idx = _binary_search(queue[-1][0], counts_pool)
                    counts_pool.insert(insertion_idx, queue[-1][0])
                    barcodes_pool.insert(insertion_idx, queue[-1][1])

                queue.pop(-1)

    if queue and queue[0][0] > 0:  # Remaining barcodes.
        rearranged_barcodes.append(queue[0][1])

    return rearranged_barcodes
