
def verify_consecutive_split(sorted_numbers: list[int]) -> bool:  # LeetCode Q.659.
    # Key: subsequences' max; value: such subsequences' respective count of length 1 & 2.
    incompletions: dict[int, dict[int, int]] = dict()
    completions = dict()  # Key: subseqs' max; value: count of all such subseqs.
    for number in sorted_numbers:
        if number - 2 in incompletions.keys():  # Incompletions can't become complete.
            return False

        if number - 1 in incompletions.keys():
            if incompletions[number - 1][1] > 0:  # Length: from 1 to 2.
                incompletions[number - 1][1] -= 1
                if incompletions[number - 1][1] == incompletions[number - 1][2] == 0:
                    del incompletions[number - 1]

                if number not in incompletions.keys():  # Subseq max: from number - 1 to number.
                    incompletions.update({number: {1: 0, 2: 0}})
                incompletions[number][2] += 1
                continue

            if incompletions[number - 1][2] > 0:  # Length: from 2 to 3.
                incompletions[number - 1][2] -= 1
                if incompletions[number - 1][1] == incompletions[number - 1][2] == 0:
                    del incompletions[number - 1]

                if number not in completions.keys():  # Subseq max: from number - 1 to number.
                    completions.update({number: 0})
                completions[number] += 1
                continue

        if number - 1 in completions.keys():  # Subseq max: from number - 1 to number.
            completions[number - 1] -= 1
            if completions[number - 1] == 0:
                del completions[number - 1]

            if number not in completions.keys():
                completions.update({number: 0})
            completions[number] += 1
            continue

        if number not in incompletions.keys():
            incompletions.update({number: {1: 0, 2: 0}})
        incompletions[number][1] += 1  # Num forms an incomplete subseq.

    return not incompletions  # Empty incompletions: split success.
