
def _swap_chars(string: str, idx_1: int, idx_2: int) -> str:
    chars = list(string)
    chars[idx_1], chars[idx_2] = chars[idx_2], chars[idx_1]
    return "".join(chars)

def sliding_puzzle(board: list[list[int]]) -> int:  # LeetCode Q.773.
    init_state = ""  # Vectorize board w.r.t. rows into string.
    for row_idx in range(2):
        for col_idx in range(3):
            init_state += str(board[row_idx][col_idx])

    visited_states: set[str] = set()  # Format: vectorize board w.r.t. rows into string.

    # Format: (current state, moves). Start from the solved state.
    queue: list[tuple[str, int]] = [("123450", 0)]
    while queue:
        state, moves = queue.pop(0)
        if state == init_state:
            return moves

        moves += 1
        visited_states.add(state)

        for idx in range(6):
            if state[idx] == "0":  # Locate the idx containing "0".
                if idx % 3 != 2:
                    state = _swap_chars(state, idx, idx + 1)
                    if state not in visited_states:
                        queue.append((state, moves))

                    state = _swap_chars(state, idx, idx + 1)  # Swap back for later usage.

                if idx % 3 != 0:
                    state = _swap_chars(state, idx, idx - 1)
                    if state not in visited_states:
                        queue.append((state, moves))

                    state = _swap_chars(state, idx, idx - 1)  # Swap back for later usage.

                if idx < 3:
                    state = _swap_chars(state, idx, idx + 3)
                    if state not in visited_states:
                        queue.append((state, moves))

                    state = _swap_chars(state, idx, idx + 3)  # Swap back for later usage.

                if idx >= 3:
                    state = _swap_chars(state, idx, idx - 3)
                    if state not in visited_states:
                        queue.append((state, moves))

                break

    return -1  # Can't be solved.
