
def count_substrings(string: str, k: int, queries: list[list[int]]) -> list[int]:  # LeetCode Q.3261.
    left_boundaries = []  # Min left idx for substrings w/ right idx at ith idx.

    zeros_counts, ones_counts = 0, 0
    prefix_substrings_counts = []

    left_idx = 0
    for right_idx in range(len(string)):
        if string[right_idx] == "1":
            ones_counts += 1

        else:
            zeros_counts += 1

        while min(zeros_counts, ones_counts) > k:
            if string[left_idx] == "1":
                ones_counts -= 1

            else:
                zeros_counts -= 1

            left_idx += 1

        left_boundaries.append(left_idx)

        if not prefix_substrings_counts:
            prefix_substrings_counts.append(0)

        else:
            prefix_substrings_counts.append(prefix_substrings_counts[-1])

        prefix_substrings_counts[-1] += right_idx + 1 - left_idx

    right_boundaries = []  # Max right idx for subarrays w/ left idx <= ith idx.

    left_idx = 0
    for right_idx in range(len(string)):
        while left_idx < len(string) and left_boundaries[left_idx] <= right_idx:
            left_idx += 1

        right_boundaries.append(left_idx - 1)

    answers = []
    for query in queries:
        start_idx, end_idx = query

        answers.append(prefix_substrings_counts[end_idx])
        if start_idx:  # Query's start idx > 0: need adjustments.
            last_affected_idx = min(right_boundaries[start_idx], end_idx)
            answers[-1] -= prefix_substrings_counts[last_affected_idx]

            total_affected_indices = (last_affected_idx + 1 - start_idx)
            answers[-1] += (1 + total_affected_indices) * total_affected_indices // 2

    return answers
