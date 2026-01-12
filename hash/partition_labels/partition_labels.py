
def partition_labels(string: str) -> list[int]:  # LeetCode Q.763.
    chars2orders: dict[str, int] = dict()
    indices_pairs: list[list[int]] = []  # Same char's 1st and last indices pair.

    for idx, char in enumerate(string):
        if char not in chars2orders.keys():
            chars2orders.update({char: len(chars2orders) + 1})
            indices_pairs.append([idx, idx])
        
        order = chars2orders[char]
        indices_pairs[order - 1][1] = idx

    partition_sizes = []
    
    current_size = 0
    current_right_idx = -1
    
    while indices_pairs:
        first_idx, last_idx = indices_pairs.pop(0)
        
        if current_right_idx < first_idx:  # Start a new partition.
            if current_size > 0:  # Store the latest partition.
                partition_sizes.append(current_size)
            
            current_size = last_idx + 1 - first_idx
            current_right_idx = last_idx
            continue
        
        if last_idx > current_right_idx:  # Current partition extends.
            current_size += last_idx - current_right_idx
            current_right_idx = last_idx
    
    if current_size > 0:  # Last remaining partition.
        partition_sizes.append(current_size)
    
    return partition_sizes
