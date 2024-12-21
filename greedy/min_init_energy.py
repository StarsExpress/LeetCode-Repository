
def calculate_min_init_energy(tasks: list[list[int]]) -> int:  # LeetCode Q.1665.
    total_actual_energy = sum(actual_energy for actual_energy, _ in tasks)
    min_init_energy = total_actual_energy  # Base case: min init energy's floor.

    # Do tasks with bigger (min energy - actual energy) first.
    tasks.sort(key=lambda x: x[0] - x[1])
    for actual_energy, min_energy in tasks:
        if total_actual_energy < min_energy:  # Need to increment.
            min_init_energy += min_energy - total_actual_energy
            total_actual_energy = min_energy
        total_actual_energy -= actual_energy

    return min_init_energy
