
def find_max_erasure(integers: list[int]):  # LeetCode Q.1695.
    if not integers:
        return 0

    max_erasure, current_erasure = 0, 0
    subarray_ints2indices, indices_pool = dict(), []

    for idx, integer in enumerate(integers):
        if integer in subarray_ints2indices.keys():  # New int is already inside subarray.
            if current_erasure > max_erasure:
                max_erasure = current_erasure

            last_occurred_idx = subarray_ints2indices[integer]
            while indices_pool and indices_pool[0] <= last_occurred_idx:
                deleted_int = integers[indices_pool.pop(0)]
                del subarray_ints2indices[deleted_int]
                current_erasure -= deleted_int  # Update current erasure.

        subarray_ints2indices.update({integer: idx})
        indices_pool.append(idx)
        current_erasure += integer

    return max(current_erasure, max_erasure)
