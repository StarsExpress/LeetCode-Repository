
def find_top_k_items(elements: list[int], k: int):  # LeetCode Q.347.
    hash_table = dict()

    for element in elements:
        if element in hash_table.keys():
            hash_table[element] += 1
            continue
        hash_table.update({element: 1})

    hash_table = dict(sorted(hash_table.items(), key=lambda item: item[1]))
    return list(hash_table.keys())[-k:]
