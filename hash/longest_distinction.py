
def find_longest_distinction(string: str):  # LeetCode Q.3.
    chars, unique_chars = list(string), set(string)
    if len(unique_chars) <= 1:
        return len(unique_chars)

    max_len, current_len = 0, 0
    subarray_chars2indices, indices_pool = dict(), []

    for idx, char in enumerate(chars):
        if char in subarray_chars2indices.keys():  # New char is already inside subarray.
            if current_len > max_len:
                max_len = current_len

            last_occurred_idx = subarray_chars2indices[char]
            while indices_pool and indices_pool[0] <= last_occurred_idx:
                deleted_char = chars[indices_pool.pop(0)]
                del subarray_chars2indices[deleted_char]
                current_len -= 1  # Update current length.

        subarray_chars2indices.update({char: idx})
        indices_pool.append(idx)
        current_len += 1

    return max(current_len, max_len)
