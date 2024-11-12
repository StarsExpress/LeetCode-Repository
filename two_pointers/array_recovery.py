
def recover_array(numbers: list[int]) -> list[int]:  # LeetCode Q.2122.
    total_numbers = len(numbers)
    if total_numbers == 2:  # Base case.
        return [sum(numbers) // 2]

    original_array_len = total_numbers // 2

    numbers.sort()
    valid_high_array_mins = []
    for idx, number in enumerate(numbers[:original_array_len + 1]):
        if (number - numbers[0]) % 2 == 0 and number > numbers[0]:
            valid_high_array_mins.append((idx, number, number - numbers[0]))

    original_array, used_indices = [], set()
    for valid_idx, valid_min, valid_diff in valid_high_array_mins:
        original_array.append((numbers[0] + valid_min) // 2)
        used_indices.update({0, valid_idx})

        back_idx, front_idx = 1, valid_idx + 1
        while True:
            while back_idx in used_indices:
                back_idx += 1

            while front_idx in used_indices:
                front_idx += 1

            if front_idx >= total_numbers:
                break

            if numbers[front_idx] - numbers[back_idx] == valid_diff:
                original_array.append(
                    (numbers[front_idx] + numbers[back_idx]) // 2
                )

                used_indices.add(back_idx)
                used_indices.add(front_idx)
                back_idx += 1

            front_idx += 1

        if len(original_array) == original_array_len:
            return original_array

        original_array.clear()
        used_indices.clear()
