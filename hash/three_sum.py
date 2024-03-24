
def find_three_sum(target: int | float, references: list[int | float] | tuple[int | float]):
    if len(references) < 3:
        raise IndexError('Three sum requires three numbers as references.')

    answers = []  # Each answer's format: (smallest_num, mid_num, biggest_num).
    references.sort()  # From smallest to biggest.

    for smallest_idx in range(len(references) - 2):
        if references[smallest_idx] > target:
            break  # All possible answers are found.

        if smallest_idx > 0 and references[smallest_idx] == references[smallest_idx - 1]:
            continue  # Reach a different smallest number.

        mid_idx, biggest_idx = smallest_idx + 1, len(references) - 1
        while True:
            if mid_idx == biggest_idx:
                break

            three_sum = references[smallest_idx] + references[mid_idx] + references[biggest_idx]
            if three_sum < target:
                mid_idx += 1  # Raise thw middle number.
                continue

            if three_sum > target:
                biggest_idx -= 1  # Reduce the biggest number.
                continue

            answer = [references[smallest_idx], references[mid_idx], references[biggest_idx]]
            answers.append(answer)

            while mid_idx < biggest_idx and references[mid_idx] == answer[1]:  # Reach a different middle number.
                mid_idx += 1
            while mid_idx < biggest_idx and references[biggest_idx] == answer[2]:  # Reach a different biggest number.
                biggest_idx -= 1

    return answers


if __name__ == '__main__':
    numbers = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    print(find_three_sum(0, numbers))
