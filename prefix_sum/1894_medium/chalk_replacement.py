
def find_chalk_replacer(chalks: list[int], upper_limit: int) -> int:  # LeetCode Q.1894.
    upper_limit %= sum(chalks)  # Only need to check mod.
    replacer = 0
    for idx, chalk in enumerate(chalks):
        upper_limit -= chalk
        if upper_limit < 0:  # This student runs out of chalks.
            replacer = idx
            break
    return replacer
