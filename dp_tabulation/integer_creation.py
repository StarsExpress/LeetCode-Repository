
def compare_digits_combo(old_combo: list[str], new_combo: list[str]) -> bool:
    """Both combos must have the same number of digits."""
    old_combo.sort(reverse=True)
    new_combo.sort(reverse=True)
    for old_digit, new_digit in zip(old_combo, new_combo):
        if old_digit > new_digit:
            return False
        if old_digit < new_digit:
            return True
    return False


def create_largest_integer(cost: list[int], target: int) -> str:  # LeetCode Q.1449.
    """Variation of coin change problem."""
    if len(set(cost)) == 1:  # Base case: all digits cost the same.
        if target % cost[-1] != 0:
            return "0"
        return "9" * (target // cost[-1])  # Always use largest digit.

    # Base case: 0 target has no digits at all.
    max_usage = [0] + [-1 for _ in range(target)]
    digits_combo = [[] for _ in range(1 + target)]

    for iter_target in range(1, target + 1):
        for digit_idx, digit_cost in enumerate(cost):
            if iter_target < digit_cost:  # Digit cost exceeds target.
                continue

            digits_usage = max_usage[iter_target - digit_cost]
            if digits_usage != -1:  # New combo found.
                digits_usage += 1  # Plus 1: usage of another digit.

                # Use copy to prevent modification on previous storage.
                used_digits = digits_combo[iter_target - digit_cost].copy()
                used_digits.append(str(digit_idx + 1))  # Another digit joins.

                if digits_usage > max_usage[iter_target]:
                    max_usage[iter_target] = digits_usage
                    digits_combo[iter_target].clear()
                    digits_combo[iter_target].extend(used_digits)
                    continue

                if digits_usage == max_usage[iter_target]:
                    if compare_digits_combo(digits_combo[iter_target], used_digits):
                        max_usage[iter_target] = digits_usage
                        digits_combo[iter_target].clear()
                        digits_combo[iter_target].extend(used_digits)

    if not digits_combo[target]:  # No digits at all.
        return "0"
    return "".join(digits_combo[target])
