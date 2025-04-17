
def _count_limited_subarrays(nums: list[int], k: int) -> int:  # LeetCode Q.3209.
    values2counts: dict[int, int] = dict()

    total_subarrays = 0
    start_idx = 0
    for end_idx, num in enumerate(nums):
        if k > num:  # Subarrays ending at current num have AND values < k.
            values2counts.clear()  # Reset.
            start_idx = end_idx + 1
            continue

        subarray_and_value = 0
        subarray_len = end_idx + 1 - start_idx

        bin_end_num = bin(num)[2:]  # Remove "0b" prefix.
        bit_idx, bit_value = -1, 1
        while bit_idx >= -len(bin_end_num):
            if bin_end_num[bit_idx] == "1":
                if bit_value not in values2counts.keys():
                    values2counts.update({bit_value: 0})
                values2counts[bit_value] += 1

                if values2counts[bit_value] == subarray_len:  # A set bit.
                    subarray_and_value += bit_value

            bit_value *= 2
            bit_idx -= 1

        while start_idx < end_idx and subarray_and_value < k:
            subarray_len -= 1

            bin_start_num = bin(nums[start_idx])[2:]  # Remove "0b" prefix.
            bit_idx, bit_value = -1, 1
            while bit_idx >= -len(bin_start_num):
                if bit_value in values2counts.keys():
                    if bin_start_num[bit_idx] == "1":
                        values2counts[bit_value] -= 1

                    if bin_start_num[bit_idx] == "0":
                        if values2counts[bit_value] == subarray_len:
                            subarray_and_value += bit_value  # A set bit.

                bit_value *= 2
                bit_idx -= 1

            while bit_idx >= -len(bin_end_num):
                if bit_value in values2counts.keys():
                    if bin_end_num[bit_idx] == "1":
                        if values2counts[bit_value] == subarray_len:
                            subarray_and_value += bit_value  # A set bit.

                bit_value *= 2
                bit_idx -= 1

            start_idx += 1

        total_subarrays += subarray_len

    return total_subarrays


def count_k_and_subarrays(nums: list[int], k: int) -> int:
    return _count_limited_subarrays(nums, k) - _count_limited_subarrays(nums, k + 1)
