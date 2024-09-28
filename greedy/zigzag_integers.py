
def count_zigzag_moves(numbers: list[int]) -> int:  # LeetCode Q.1144.
    odd_indexed_numbers, odd_moves = numbers.copy(), 0  # Use copy to separate modification.
    even_indexed_nums, even_moves = numbers.copy(), 0  # Use copy to separate modification.
    total_numbers = len(numbers)

    for i in range(total_numbers // 2):  # Make every odd-indexed > adjacent numbers.
        if odd_indexed_numbers[2 * i] >= odd_indexed_numbers[2 * i + 1]:
            move = odd_indexed_numbers[2 * i] + 1 - odd_indexed_numbers[2 * i + 1]
            odd_indexed_numbers[2 * i] -= move  # Only decrement is allowed.
            odd_moves += move

        if 2 * i + 2 < total_numbers:
            if odd_indexed_numbers[2 * i + 2] >= odd_indexed_numbers[2 * i + 1]:
                move = odd_indexed_numbers[2 * i + 2] + 1 - odd_indexed_numbers[2 * i + 1]
                odd_indexed_numbers[2 * i + 2] -= move  # Only decrement is allowed.
                odd_moves += move

    for i in range(total_numbers // 2):  # Make every even-indexed > adjacent numbers.
        if even_indexed_nums[2 * i + 1] >= even_indexed_nums[2 * i]:
            move = even_indexed_nums[2 * i + 1] + 1 - even_indexed_nums[2 * i]
            even_indexed_nums[2 * i + 1] -= move  # Only decrement is allowed.
            even_moves += move

        if 2 * i + 2 < total_numbers:
            if even_indexed_nums[2 * i + 1] >= even_indexed_nums[2 * i + 2]:
                move = even_indexed_nums[2 * i + 1] + 1 - even_indexed_nums[2 * i + 2]
                even_indexed_nums[2 * i + 1] -= move  # Only decrement is allowed.
                even_moves += move

    return min(odd_moves, even_moves)
