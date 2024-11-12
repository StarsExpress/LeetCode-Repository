
def find_min_jumps(numbers: list[int]) -> int:  # LeetCode Q.45.
    total_numbers, jumps = len(numbers), 0
    destination_idx = total_numbers - 1  # Reverse jump game: from rightmost to leftmost number.

    while destination_idx > 0:  # Haven't reached the leftmost number.
        leftmost_reachable_idx = None
        for idx, number in enumerate(numbers[:destination_idx]):
            if number >= destination_idx - idx:
                leftmost_reachable_idx = idx
                break

        jumps += 1  # Jump from destination idx's number to leftmost reachable idx's number.
        destination_idx = leftmost_reachable_idx  # Update the newest destination idx.

    return jumps


def verify_jump_availability(numbers: list[int]) -> bool:  # LeetCode Q.55.
    total_numbers = len(numbers)
    destination_idx = -1  # Reverse jump game: from rightmost to leftmost number.

    while destination_idx > -total_numbers:  # Haven't reached the leftmost number.
        for idx, number in enumerate(numbers[:destination_idx][::-1]):
            if number >= 1 + idx:  # Current number & destination's idx diff = 1 + idx.
                destination_idx -= (1 + idx)  # Update the newest destination idx.
                break  # Continue to while loop's next iteration.

        else:  # For loop doesn't break: can't reach destination.
            return False

    return True
