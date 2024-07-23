
def find_min_squares_usage(area: int):  # LeetCode Q.279.
    """Fin min number of perfect squares to form area."""
    max_sqrt = int(area ** 0.5)  # Find all squares <= area.
    perfect_squares = [sqrt ** 2 for sqrt in range(1, max_sqrt + 1)]

    min_combo = [0] + [float("inf")] * area  # Base case.

    for target_square in range(1, area + 1):
        for square in perfect_squares:
            if target_square - square >= 0:  # Current square can be used.
                # Plus 1: usage of current square.
                new_combo = min_combo[target_square - square] + 1
                if new_combo < min_combo[target_square]:
                    min_combo[target_square] = new_combo

    return min_combo[area]
