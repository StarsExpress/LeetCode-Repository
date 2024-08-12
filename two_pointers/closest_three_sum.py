
def find_closest_3_sum(target: int | float, references: list[int | float]):  # LeetCode Q.16.
    references_count = len(references)

    references.sort()
    answer, closest_diff = None, float("inf")

    for smallest_idx in range(references_count - 2):
        mid_idx, biggest_idx = smallest_idx + 1, references_count - 1

        while mid_idx < biggest_idx:
            diff = references[smallest_idx] + references[mid_idx] + references[biggest_idx] - target
            if diff == 0:
                return references[smallest_idx] + references[mid_idx] + references[biggest_idx]

            if abs(diff) <= closest_diff:
                closest_diff = abs(diff)
                answer = references[smallest_idx] + references[mid_idx] + references[biggest_idx]

            if diff < 0:
                mid_idx += 1
                continue

            biggest_idx -= 1

    return answer
