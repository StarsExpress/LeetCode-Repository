
def find_3_sum(references: list[int | float], target: int | float):  # LeetCode Q.15.
    references_count = len(references)

    references.sort()  # From smallest to biggest.
    answers = []  # Each answer's format: (smallest num, mid num, biggest num).

    for smallest_idx in range(references_count - 2):
        if references[smallest_idx] > target:
            break  # All possible answers are found.

        if smallest_idx > 0 and references[smallest_idx] == references[smallest_idx - 1]:
            continue  # Reach a different smallest number.

        mid_idx, biggest_idx = smallest_idx + 1, references_count - 1
        while mid_idx != biggest_idx:
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
