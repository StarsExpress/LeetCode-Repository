
def count_almost_equal_pairs(nums: list[int]) -> int:  # LeetCode Q.3267.
    new_nums_table: dict[int, set[int]] = dict()  # Each num's transformed nums set.

    old_nums2counts: dict[int, float] = dict()
    new_nums2counts: dict[int, float] = dict()

    queue: list[int] = []
    new_nums: set[int] = set()
    for num in nums:
        if num not in old_nums2counts.keys():
            old_nums2counts.update({num: 0})
        old_nums2counts[num] += 1

        if num not in new_nums_table.keys():
            queue.append(num)

            rounds = 2
            while rounds > 0:
                transformations = len(queue)
                while transformations > 0:
                    new_num = queue.pop(0)
                    digits = list(str(new_num))
                    new_num_len = len(digits)

                    for back_idx in range(new_num_len - 1):
                        for front_idx in range(back_idx + 1, new_num_len):
                            digits[back_idx], digits[front_idx] = digits[front_idx], digits[back_idx]

                            new_num = int("".join(digits))
                            if new_num != num and new_num not in new_nums:
                                new_nums.add(new_num)  # Only take real new nums.
                                queue.append(new_num)

                            digits[back_idx], digits[front_idx] = digits[front_idx], digits[back_idx]

                    transformations -= 1

                rounds -= 1

            new_nums_table.update({num: new_nums.copy()})  # Copy: prevent modification.
            queue.clear()
            new_nums.clear()

        num_len = len(str(num))
        for new_num in new_nums_table[num]:
            if new_num not in new_nums2counts.keys():
                new_nums2counts.update({new_num: 0})
            new_nums2counts[new_num] += 1

            if len(str(new_num)) == num_len:
                new_nums2counts[new_num] -= 0.5

    almost_equal_pairs = 0
    for _, count in old_nums2counts.items():
        almost_equal_pairs += count * (count - 1) // 2

    for num in nums:
        if num in new_nums2counts.keys():
            almost_equal_pairs += new_nums2counts[num]

    return int(almost_equal_pairs)  # Return int form.
