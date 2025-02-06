
def count_max_visited_indices(numbers: list[int], distance: int) -> int:  # LeetCode Q.1340.
    total_nums = len(numbers)
    max_visited_count, max_visited_indices = 1, [1] * total_nums  # Base case.

    nums2indices = dict()
    for idx, num in enumerate(numbers):
        if num not in nums2indices.keys():
            nums2indices.update({num: []})
        nums2indices[num].append(idx)

    nums2indices = dict(sorted(nums2indices.items()))
    for num, indices in nums2indices.items():
        for idx in indices:
            visit_ranges = [
                range(idx - 1, max(idx - distance, 0) - 1, -1),  # Reverse: leftward visit.
                range(idx + 1, min(idx + distance + 1, total_nums))  # Rightward visit.
            ]
            for visit_range in visit_ranges:
                for visit_idx in visit_range:
                    if numbers[visit_idx] >= num:  # End search upon a non-smaller num.
                        break

                    visited_indices = 1 + max_visited_indices[visit_idx]
                    if visited_indices > max_visited_indices[idx]:
                        max_visited_indices[idx] = visited_indices

                    if visited_indices > max_visited_count:
                        max_visited_count = visited_indices

    return max_visited_count
