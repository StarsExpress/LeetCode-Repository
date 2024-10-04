
def count_min_rabbits(answers: list[int]) -> int:  # LeetCode Q.781.
    min_rabbits, non_zero_answers2counts = 0, dict()
    for answer in answers:
        if answer + 1 not in non_zero_answers2counts.keys():
            non_zero_answers2counts.update({answer + 1: 0})
        non_zero_answers2counts[answer + 1] += 1

    for answer, count in non_zero_answers2counts.items():
        groups = count // answer
        if count % answer > 0:  # Another group of rabbits.
            groups += 1
        min_rabbits += groups * answer

    return min_rabbits
