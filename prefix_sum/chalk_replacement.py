
def find_chalk_replacer(chalks: list[int], upper_limit: int):  # LeetCode Q.1894.
    total_chalks = sum(chalks)
    upper_limit %= total_chalks  # Only need to check mod.
    for idx, chalk in enumerate(chalks):
        upper_limit -= chalk
        if upper_limit < 0:  # This student runs out of chalks.
            return idx
