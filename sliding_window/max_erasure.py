
def find_max_erasure(integers: list[int]):  # LeetCode Q.1695.
    if len(integers) <= 0:
        return 0
    if len(set(integers)) == 1:
        return integers[0]

    start_idx, end_idx = 0, 1  # Iteration starts from 2nd int.
    max_erasure, current_erasure = integers[0], integers[0]
    while True:
        if end_idx >= len(integers):  # Reach input's end.
            return max(current_erasure, max_erasure)

        # Candidate int is in "somewhere" of window.
        if integers[end_idx] in integers[start_idx: end_idx]:
            if current_erasure > max_erasure:
                max_erasure = current_erasure  # Update erasure.

            # Candidate int's window location.
            start_idx += integers[start_idx: end_idx].index(integers[end_idx])
            start_idx += 1  # Now candidate int isn't the newest window.
            current_erasure = sum(integers[start_idx: end_idx])

        current_erasure += integers[end_idx]
        end_idx += 1  # Go to next int.


if __name__ == '__main__':
    numbers = [4, 2, 4, 5, 6]
    print(find_max_erasure(numbers))
