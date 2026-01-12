
def rot_oranges(grid: list[list[int]]) -> int:  # LeetCode Q.994.
    current_rot: list[tuple[int, int]] = []  # Foramt: (row idx, col idx).
    next_rot: list[tuple[int, int]] = []  # Format: (row idx, col idx).
    
    fresh_oranges: dict[tuple[int, int], bool] = dict()
    for row_idx, row in enumerate(grid):
        for col_idx, entry in enumerate(row):
            if entry == 2:
                current_rot.append((row_idx, col_idx))
            
            elif entry == 1:
                fresh_oranges[(row_idx, col_idx)] = True
    
    spent_mins = 0
    while current_rot:
        row_idx, col_idx = current_rot.pop(0)
        
        neighbors = [
            (row_idx - 1, col_idx), (row_idx, col_idx + 1),
            (row_idx + 1, col_idx), (row_idx, col_idx - 1)
        ]
        
        for neighbor_row_idx, neighbor_col_idx in neighbors:
            if 0 <= neighbor_row_idx < len(grid):
                if 0 <= neighbor_col_idx < len(grid[0]):
                    if grid[neighbor_row_idx][neighbor_col_idx] == 1:
                        grid[neighbor_row_idx][neighbor_col_idx] += 1
                        del fresh_oranges[(neighbor_row_idx, neighbor_col_idx)]
                        next_rot.append((neighbor_row_idx, neighbor_col_idx))
        
        if not current_rot and next_rot:
            spent_mins += 1
            current_rot.extend(next_rot.copy())
            next_rot.clear()
    
    # Fresh orange still exists: return -1 as impossible.
    return -1 if fresh_oranges else spent_mins
