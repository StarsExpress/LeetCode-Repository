
def count_min_jumps(numbers: list[int]) -> int:  # LeetCode Q.1345.
    total_numbers, numbers2indices = len(numbers), dict()
    for idx, number in enumerate(numbers):
        if number not in numbers2indices.keys():
            numbers2indices.update({number: []})
        numbers2indices[number].append(idx)

    visited_indices, jumps = {0}, 0
    queue = [(0, jumps)]  # Format: (current index, jumps made).
    while queue:
        current_idx, jumps = queue.pop(0)
        if current_idx == total_numbers - 1:
            break

        for neighbor in [current_idx - 1, current_idx + 1]:
            if 0 <= neighbor < total_numbers and neighbor not in visited_indices:
                queue.append((neighbor, jumps + 1))
                visited_indices.add(neighbor)

        number = numbers[current_idx]
        for neighbor in numbers2indices[number]:
            if neighbor not in visited_indices:
                queue.append((neighbor, jumps + 1))
                visited_indices.add(neighbor)

        numbers2indices[number].clear()  # Avoid reprocessing.

    return jumps
