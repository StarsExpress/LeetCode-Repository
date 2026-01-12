
def generate_spiral_matrix(n: int) -> list[list[int]]:  # LeetCode Q.59.
    matrix: list[list[int]] = [[0] * n for _ in range(n)]
    matrix[0][0] = 1

    row_idx, col_idx = 0, 0
    current_num = 2

    total_entries = n ** 2
    unfilled: dict[int, bool] = dict(
        zip(
            range(2, total_entries + 1), [True] * (total_entries - 1)
        )
    )  # 1 at top left has already been filled by default.
    
    direction = "right"  # Direction priorities: right, down, left, up.
    
    while unfilled:
        if direction == "right":
            if col_idx + 1 < n:
                if matrix[row_idx][col_idx + 1] == 0:
                    col_idx += 1
                    matrix[row_idx][col_idx] += current_num
                    del unfilled[current_num]
                    current_num += 1
                    continue

            direction = "down"
            continue
        
        elif direction == "down":
            if row_idx + 1 < n:
                if matrix[row_idx + 1][col_idx] == 0:
                    row_idx += 1
                    matrix[row_idx][col_idx] += current_num
                    del unfilled[current_num]
                    current_num += 1
                    continue
            
            direction = "left"
            continue
        
        elif direction == "left":
            if col_idx - 1 >= 0:
                if matrix[row_idx][col_idx - 1] == 0:
                    col_idx -= 1
                    matrix[row_idx][col_idx] += current_num
                    del unfilled[current_num]
                    current_num += 1
                    continue
            
            direction = "up"
            continue
        
        if row_idx - 1 >= 0:
            if matrix[row_idx - 1][col_idx] == 0:
                row_idx -= 1
                matrix[row_idx][col_idx] += current_num
                del unfilled[current_num]
                current_num += 1
                continue

        direction = "right"
            
    return matrix
