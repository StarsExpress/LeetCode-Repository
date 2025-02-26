
def _find_best_candidate(candidates: list[list[int]]) -> tuple[int, int]:
    # Each candidate's format: [best sum, best sum's paths count].
    candidates.sort(reverse=True)
    best_score, paths_count = candidates[0][0], candidates[0][1]
    for candidate in candidates[1:]:
        if candidate[0] == best_score:
            paths_count += candidate[1]
    return best_score, paths_count


def count_max_score_paths(board: list[str]) -> list[int]:  # LeetCode Q.1301.
    # Use for loop to create matrix with separate list entries.
    # Each entry's format: [best sum, best sum's paths count].
    matrix = [[[0, 0] for _ in range(len(board[i]))] for i in range(len(board))]
    candidates = []  # List of lists of potential best sum & paths count for each entry.

    best_score_paths_count = []  # Format: [best sum, its paths count].
    for row_idx, row in enumerate(reversed(board)):
        entries = list(row)
        for col_idx, entry in enumerate(reversed(entries)):
            if entry == "S":  # Base case: start point's paths count is 1.
                matrix[-row_idx - 1][-col_idx - 1][1] += 1
                continue

            if entry == "X":  # Obstacle.
                continue

            if entry == "E":  # Destination.
                candidates.append(matrix[-row_idx - 1][-col_idx])  # Right.
                candidates.append(matrix[-row_idx][-col_idx - 1])  # Bottom.
                candidates.append(matrix[-row_idx][-col_idx])  # Slant.

                best_score, paths_count = _find_best_candidate(candidates)
                best_score_paths_count.extend([best_score, paths_count % (10 ** 9 + 7)])
                break  # Answer is found: take modulo to control final paths count.

            if col_idx == 0:  # Entry only has bottom neighbor.
                if matrix[-row_idx][-1][1] != 0:  # Bottom neighbor isn't obstacle.
                    # Update paths count.
                    matrix[-row_idx - 1][-1][1] += matrix[-row_idx][-1][1]
                    # Update best score.
                    matrix[-row_idx - 1][-1][0] += int(entry) + matrix[-row_idx][-1][0]

                continue

            if row_idx == 0:  # Entry only has right neighbor.
                if matrix[-1][-col_idx][1] != 0:  # Right neighbor isn't obstacle.
                    # Update paths count.
                    matrix[-1][-col_idx - 1][1] += matrix[-1][-col_idx][1]
                    # Update best score.
                    matrix[-1][-col_idx - 1][0] += int(entry) + matrix[-1][-col_idx][0]

                continue

            if col_idx != 0:  # Entry has bottom, right and slant neighbors.
                if {
                    matrix[-row_idx - 1][-col_idx][1],  # Right.
                    matrix[-row_idx][-col_idx - 1][1],  # Bottom.
                    matrix[-row_idx][-col_idx][1],  # Slant.
                } != {0}:  # At least one neighbor isn't obstacle.

                    candidates.append(matrix[-row_idx - 1][-col_idx])  # Right.
                    candidates.append(matrix[-row_idx][-col_idx - 1])  # Bottom.
                    candidates.append(matrix[-row_idx][-col_idx])  # Slant.

                    best_score, paths_count = _find_best_candidate(candidates)
                    # Update paths count.
                    matrix[-row_idx - 1][-col_idx - 1][1] += paths_count
                    # Update best score.
                    matrix[-row_idx - 1][-col_idx - 1][0] += int(entry) + best_score

                    candidates.clear()

    return best_score_paths_count
