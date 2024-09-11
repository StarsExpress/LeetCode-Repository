
def query_xor(arr: list[int], queries: list[list[int]]) -> list[int]:  # LeetCode Q.1310.
    xor_values = []
    for num in arr:
        if not xor_values:
            xor_values.append(num)
            continue
        xor_values.append(xor_values[-1] ^ num)

    results = []
    for left_idx, right_idx in queries:
        if left_idx == 0:
            results.append(xor_values[right_idx])
            continue
        results.append(xor_values[left_idx - 1] ^ xor_values[right_idx])

    return results
