
def find_max_length(nums: list[int], k: int) -> int:  # LeetCode Q.3177.
    max_len = 1  # Base case.

    # ith idx stores best subseq len when using only nums[:i + 1].
    prev_diff_best, current_diff_best = [], []  # Only need latest 2 diffs.

    # At current diff, each num's best subseq len when served as subseq end.
    nums2lens: dict[int, int] = dict()
    for diff in range(k + 1):  # Differences go from 0 to k.
        for idx, num in enumerate(nums):
            if num in nums2lens.keys():  # Extend subseq w/o changing diff.
                nums2lens[num] += 1

            else:
                nums2lens.update({num: 1})  # Base case.

            if min(diff, idx) > 0:  # Can extend previous diff's earlier subseqs.
                if prev_diff_best[idx - 1] + 1 > nums2lens[num]:
                    nums2lens[num] = prev_diff_best[idx - 1] + 1

            if current_diff_best and nums2lens[num] <= current_diff_best[-1]:
                current_diff_best.append(current_diff_best[-1])

            else:
                current_diff_best.append(nums2lens[num])
                if nums2lens[num] > max_len:
                    max_len = nums2lens[num]

        prev_diff_best.clear()  # Reset for the next diff.
        prev_diff_best.extend(current_diff_best)
        current_diff_best.clear()
        nums2lens.clear()

    return max_len
