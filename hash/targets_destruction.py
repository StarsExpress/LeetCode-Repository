
def destroy_targets(integers: list[int], space: int):  # LeetCode Q.2453.
    if len(integers) == 1:
        return integers[0]

    mods_table, current_mod, current_seed = dict(), 0, float('inf')
    for integer in integers:  # Group by each int's modulo over space.
        current_mod += (integer % space) - current_mod
        if current_mod not in mods_table.keys():
            mods_table.update({current_mod: []})  # List tracks members of each modulo.
        mods_table[current_mod].append(integer)
        if integer < current_seed:
            current_seed = integer  # Default current seed is min int.

    max_destruction, current_destruction = 0, 0
    best_seed = current_seed  # Default best seed is min int.

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
