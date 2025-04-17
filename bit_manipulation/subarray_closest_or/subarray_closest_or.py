
def count_closest_subarray_or(nums: list[int], k: int) -> int:  # LeetCode Q.3171.
    min_abs_diff = float("inf")
    subarray_or_value = 0
    values2counts: dict[int, int] = dict()

    left_idx = 0
    for right_idx, num in enumerate(nums):
        bin_right_num = bin(num)[2:]  # Remove "0b" prefix.

        bit_idx, bit_value = -1, 1
        while bit_idx >= -len(bin_right_num):
            if bin_right_num[bit_idx] == "1":
                if bit_value not in values2counts.keys():
                    values2counts.update({bit_value: 0})
                values2counts[bit_value] += 1

                if values2counts[bit_value] == 1:
                    subarray_or_value += bit_value

            bit_value *= 2
            bit_idx -= 1

        while left_idx < right_idx and subarray_or_value > k:
            bin_left_num = bin(nums[left_idx])[2:]  # Remove "0b" prefix.
            bit_idx, bit_value = -1, 1
            left_num_deducted_values = 0
            while bit_idx >= -len(bin_left_num):
                if bin_left_num[bit_idx] == "1":
                    values2counts[bit_value] -= 1
                    if values2counts[bit_value] == 0:
                        left_num_deducted_values += bit_value

                bit_value *= 2
                bit_idx -= 1

            subarray_or_value -= left_num_deducted_values
            if subarray_or_value <= k:
                abs_diff = subarray_or_value + left_num_deducted_values - k
                if abs_diff < min_abs_diff:
                    min_abs_diff = abs_diff

            left_idx += 1

        abs_diff = abs(subarray_or_value - k)
        if abs_diff == 0:  # Early exit.
            return 0
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff

    return min_abs_diff
