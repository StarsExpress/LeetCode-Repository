
def count_substrings(string: str, character: str):  # LeetCode Q.3084.
    # Count substrings that start and end with certain character.
    count = list(string).count(character)
    return (count + 1) * count // 2  # Sum of 1 to n.
