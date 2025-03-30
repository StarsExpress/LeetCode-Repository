
def count_good_partitions(nums: list[int]) -> int:  # LeetCode Q.2963.
    nums2ranges = dict()  # Key: num; value: 1st and last occurred indices.
    for idx, num in enumerate(nums):
        if num not in nums2ranges.keys():
            nums2ranges.update({num: [idx, idx]})
        nums2ranges[num][1] = idx  # Update last occurred idx.

    total_segments = 0
    last_segment_first_idx, last_segment_last_idx = -1, -1
    for first_idx, last_idx in nums2ranges.values():
        if first_idx <= last_segment_last_idx:  # Merge current and last segments.
            last_segment_last_idx = max(last_segment_last_idx, last_idx)
            continue
        last_segment_first_idx, last_segment_last_idx = first_idx, last_idx
        total_segments += 1  # Isolate current segment.

    return (2 ** (total_segments - 1)) % (10 ** 9 + 7)  # Required to control size.
