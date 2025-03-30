
def compute_total_strengths(strengths: list[int]) -> int:  # LeetCode Q.2281.
    prefix_sums: list[int] = []
    prefix_prefix_sums: list[int] = []
    for idx, strength in enumerate(strengths):
        if idx == 0:
            prefix_sums.append(strength)
            prefix_prefix_sums.append(strength)

        else:
            prefix_sums.append(prefix_sums[-1] + strength)
            prefix_prefix_sums.append(prefix_prefix_sums[-1] + prefix_sums[-1])

    total_strengths = 0
    strengths_sum = [0] * len(strengths)  # Total strengths of subarrays ending at ith idx.

    stack = []  # Format: (idx, strength).
    prev_min_strength_idx = -1  # Idx of the prev min strength.
    # Sum of subarrays ending at current min strength idx.
    min_strength_subarrays_sum = 0

    modulo = 10 ** 9 + 7
    subarrays_mins_sum: dict[int, int] = dict()  # Sum of mins of subarrays ending at ith idx.
    for idx, strength in enumerate(strengths):
        while stack and stack[-1][1] >= strength:
            stack.pop()

        if not stack:  # Current strength < all past strengths.
            # Track strengths after prev min strength and until current strength.
            for between_idx in range(prev_min_strength_idx + 1, idx + 1):
                # In-between strength's weight = its idx + 1.
                min_strength_subarrays_sum += strengths[between_idx] * (between_idx + 1)

            strengths_sum[idx] += min_strength_subarrays_sum * strength
            prev_min_strength_idx = idx

        else:  # Current strength has prev smaller strength.
            smaller_idx = stack[-1][0]
            between_count = idx - smaller_idx

            strengths_sum[idx] += strengths_sum[smaller_idx]

            if smaller_idx not in subarrays_mins_sum.keys():
                subarrays_mins_sum[smaller_idx] = strengths[smaller_idx] * (smaller_idx + 1)

            mins_sum = subarrays_mins_sum[smaller_idx]

            strengths_sum[idx] += (prefix_sums[idx] - prefix_sums[smaller_idx]) * mins_sum

            subarrays_mins_sum[idx] = mins_sum + strength * between_count

            prefix_prefix_sum = between_count * prefix_sums[idx]
            subtract_term = prefix_prefix_sums[idx - 1]
            if smaller_idx >= 1:
                subtract_term -= prefix_prefix_sums[smaller_idx - 1]

            strengths_sum[idx] += (prefix_prefix_sum - subtract_term) * strength

        strengths_sum[idx] %= modulo
        total_strengths += strengths_sum[idx]
        stack.append((idx, strength))

    return total_strengths % modulo
