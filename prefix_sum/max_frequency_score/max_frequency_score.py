
def maximize_frequency_score(nums: list[int], limit: int) -> int:  # LeetCode Q.2968.
    nums.sort()
    prefix_sums = []
    for num in nums:
        if not prefix_sums:
            prefix_sums.append(num)
            continue
        prefix_sums.append(prefix_sums[-1] + num)

    max_score = 1  # Base case.

    left_idx, mid_idx = 0, 0
    for right_idx in range(len(nums)):
        first_while = True
        while True:
            if not first_while:
                left_idx += 1  # Since 2nd while, the subarray left bound rises.

            # Always optimal to change all nums to the num at mid idx.
            mid_idx = (left_idx + right_idx) // 2
            operations = prefix_sums[right_idx] - prefix_sums[mid_idx]
            operations -= nums[mid_idx] * (right_idx - mid_idx)

            operations += nums[mid_idx] * (mid_idx - left_idx)
            if mid_idx > 0:
                operations -= prefix_sums[mid_idx - 1]
                if left_idx > 0:
                    operations += prefix_sums[left_idx - 1]

            if limit >= operations or left_idx == right_idx:
                break
            first_while = False

        score = right_idx + 1 - left_idx
        if score > max_score:
            max_score = score

    return max_score
