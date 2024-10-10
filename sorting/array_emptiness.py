
def count_operations_to_empty_array(numbers: list[int]) -> int:  # LeetCode Q.2659.
    nums_indices_list, total_numbers = [], 0
    for idx, number in enumerate(numbers):
        total_numbers += 1
        nums_indices_list.append([number, idx])
    nums_indices_list.sort()  # Sort by ascending values.

    operations = total_numbers  # Minimum operations.
    for idx in range(1, total_numbers):
        # Extra operations happen when smaller idx points to higher values.
        if nums_indices_list[idx - 1][1] > nums_indices_list[idx][1]:
            operations += total_numbers - idx  # The closer to array's end, the shorter to wait.

    return operations
