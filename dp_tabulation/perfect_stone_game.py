
def judge_winnability(stones: int) -> bool:  # LeetCode Q.1510.
    # Idx = remaining stones.
    outcomes = [False, True]  # Base cases: 0 stone => lose, and 1 stone => win.
    remaining_stones = 2  # Start from the case of 2 remaining stones.
    while remaining_stones <= stones:
        max_sqrt = int(remaining_stones ** 0.5)
        for sqrt in range(max_sqrt, 0, -1):
            if not outcomes[remaining_stones - sqrt ** 2]:
                outcomes.append(True)  # A winning method is found.
                break

        else:
            outcomes.append(False)

        remaining_stones += 1

    return outcomes[-1]
