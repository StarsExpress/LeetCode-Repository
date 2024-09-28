
def make_sequence(target: list[int], array: list[int]) -> int:  # LeetCode Q.1713.
    nums2indices, total_targets = dict(), 0
    for idx, number in enumerate(target):  # Target array is distinct.
        nums2indices.update({number: idx})
        total_targets += 1

    new_arr = []
    for number in array:
        if number in nums2indices.keys():
            new_arr.append(nums2indices[number])

    rising_subsequence, subsequence_len = [], 0
    for number in new_arr:
        # After binary search is over, back idx is insertion idx.
        back_idx, front_idx = 0, subsequence_len - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if rising_subsequence[mid_idx] < number:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        if back_idx == subsequence_len:
            rising_subsequence.append(number)
            subsequence_len += 1

        else:
            rising_subsequence[back_idx] = number

    return total_targets - subsequence_len  # Min operations needed to make sequence.
