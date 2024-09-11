
def decode_permutation(encoded: list[int]) -> list[int]:  # LeetCode Q.1734.
    total_encoded = len(encoded)
    integers_range = total_encoded + 1  # Permutation range: 1 to n.
    first_permutation = 0
    for integer in range(1, integers_range + 1):
        first_permutation ^= integer

    total_odd_indices = total_encoded // 2
    for i in range(total_odd_indices):  # XOR all odd indices' encoded input.
        first_permutation ^= encoded[2 * i + 1]

    permutation = [first_permutation]
    for i in range(total_encoded):  # Get 2nd to last permutation.
        permutation.append(permutation[-1] ^ encoded[i])

    return permutation
