
def _binary_search(target: int, sorted_integers: list[int], size: int) -> int:
    left_idx, right_idx = 0, size - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_integers[mid_idx] <= target:
            left_idx = mid_idx + 1
            continue
        right_idx = mid_idx - 1

    return left_idx  # Number of ints <= target.


def count_bloom_flowers(flowers: list[list[int]], people: list[int]) -> list[int]:  # LeetCode Q.2251.
    start_times, end_times = [], []
    for start_time, end_time in flowers:
        start_times.append(start_time)
        end_times.append(end_time + 1)

    start_times.sort()
    start_times_prefix_counts = []
    for idx, start_time in enumerate(start_times):
        if idx == 0:
            start_times_prefix_counts.append(1)
            continue

        if start_time > start_times[idx - 1]:
            start_times_prefix_counts.append(start_times_prefix_counts[-1])

        start_times_prefix_counts[-1] += 1

    start_times = sorted(set(start_times))
    unique_start_times_count = len(start_times)

    end_times.sort()
    end_times_prefix_counts = []
    for idx, end_time in enumerate(end_times):
        if idx == 0:
            end_times_prefix_counts.append(1)
            continue

        if end_time > end_times[idx - 1]:
            end_times_prefix_counts.append(end_times_prefix_counts[-1])

        end_times_prefix_counts[-1] += 1

    end_times = sorted(set(end_times))
    unique_end_times_count = len(end_times)

    full_bloom_flowers = [0] * len(people)
    for person_idx, arrival_time in enumerate(people):
        search_idx = _binary_search(
            arrival_time, start_times, unique_start_times_count
        )
        if search_idx == 0:  # All the time pairs have start <= end.
            continue

        full_bloom_flowers[person_idx] += start_times_prefix_counts[search_idx - 1]
        search_idx = _binary_search(
            arrival_time, end_times, unique_end_times_count
        )
        if search_idx > 0:
            full_bloom_flowers[person_idx] -= end_times_prefix_counts[search_idx - 1]

    return full_bloom_flowers
