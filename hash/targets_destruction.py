
def destroy_targets(integers: list[int], space: int):  # LeetCode Q.2453.
    if len(integers) == 1:
        return integers[0]

    mods_table, current_mod = dict(), 0
    for integer in integers:  # Group by each integer's modulo overt space.
        current_mod += (integer % space) - current_mod
        if current_mod not in mods_table.keys():
            mods_table.update({current_mod: []})

        mods_table[current_mod].append(integer)

    max_destruction, current_destruction = 0, 0
    current_seed = min(integers)
    best_seed = current_seed

    for mods in mods_table.values():
        current_destruction += len(mods) - current_destruction
        if current_destruction <= 0:  # Can just skip to next round.
            continue

        current_seed += min(mods) - current_seed

        if current_destruction > max_destruction:
            max_destruction += current_destruction - max_destruction
            best_seed += current_seed - best_seed

        if current_destruction == max_destruction:  # When a tie happens, pick the smallest seed.
            if current_seed < best_seed:
                best_seed += current_seed - best_seed

    return best_seed
