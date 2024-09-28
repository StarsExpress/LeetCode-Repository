
def find_winning_senate(senate: str) -> str:  # LeetCode Q.649.
    """Key: always ban opponent's highest-ordered (the next) senator in current round."""
    dire_party, dire_count = [], 0
    radiant_party, radiant_count = [], 0
    for idx, senator in enumerate(senate):
        if senator == "D":
            dire_party.append(idx)
            dire_count += 1

        else:
            radiant_party.append(idx)
            radiant_count += 1

    senator_idx = 0  # Which senator is exercising now.
    while min(dire_count, radiant_count) > 1:
        if dire_party[0] == senator_idx:
            dire_party.append(dire_party.pop(0))  # Go to the back: wait for next round.
            radiant_count -= 1
            radiant_party.pop(0)

        if radiant_party[0] == senator_idx:
            radiant_party.append(radiant_party.pop(0))  # Go to the back: wait for next round.
            dire_count -= 1
            dire_party.pop(0)

        smaller_idx = min(dire_party[0], radiant_party[0])
        bigger_idx = max(dire_party[0], radiant_party[0])
        if smaller_idx > senator_idx or bigger_idx < senator_idx:
            senator_idx = smaller_idx
            continue

        senator_idx = bigger_idx

    if dire_count == radiant_count:  # Both party have 1 senator.
        return "Dire" if senate[0] == "D" else "Radiant"
    return "Dire" if dire_count > radiant_count else "Radiant"
