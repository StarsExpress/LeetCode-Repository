
def form_no_triplet_string(a: int, b: int) -> str:  # LeetCode Q.984.
    string, current_end = "", ""
    while max(a, b) > 0:
        if a == 0:
            return string + "b" * b

        if b == 0:
            return string + "a" * a

        if a == b:
            if a == 1:
                return string + "ab" if current_end == "b" else string + "ba"

            if current_end == "b":
                string += "aabb"

            else:
                string += "bbaa"

            a -= 2
            b -= 2
            continue

        if a > b:
            string += "aab"
            current_end = "b"
            a -= 2
            b -= 1
            continue

        string += "bba"
        current_end = "a"
        a -= 1
        b -= 2

    return string
