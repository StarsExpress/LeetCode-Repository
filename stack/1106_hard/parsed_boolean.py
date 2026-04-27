
def parse_bool_expression(expression: str) -> bool:  # LeetCode Q.1106.
    left_parentheses_indices: list[int] = []
    evaluations: list[list[int]] = []  # Format: [idx, evaluation value].

    for idx, char in enumerate(expression):
        if char == "(":  # Left parenthesis' left neighbor must be a logical operator.
            left_parentheses_indices.append(idx)

        if char == ")":
            pair_idx = left_parentheses_indices.pop(-1)
            if expression[pair_idx - 1] == "!":  # No need to merge within parentheses.
                evaluations[-1][1] ^= 1  # Flip by XOR to reflect NOT operator.

            else:  # Merge evaluations by logical operators.
                merged_evaluation = evaluations.pop(-1)[1]
                while evaluations and pair_idx < evaluations[-1][0] < idx:
                    if expression[pair_idx - 1] == "&":
                        merged_evaluation &= evaluations.pop(-1)[1]
                    if expression[pair_idx - 1] == "|":
                        merged_evaluation |= evaluations.pop(-1)[1]

                evaluations.append([pair_idx, merged_evaluation])

        if char in {"t", "f"}:
            evaluation = 1 if char == "t" else 0
            evaluations.append([idx, evaluation])

    return bool(evaluations[0][1])  # Only remaining evaluation is the final answer.
