
def replace_strings(string: str, indices: list[int], sources: list[str], targets: list[str]):  # LeetCode Q.833.
    if not len(indices) == len(sources) == len(targets):
        raise IndexError('Indices, sources and targets must have the same length.')

    chars, assembly = list(string), []  # Decompose string into chars. Store chars of final assembly.
    chars_idx, source_idx = 0, 0
    while True:
        if chars_idx >= len(chars):
            return ''.join(assembly)

        if chars_idx in indices:
            source_idx += indices.index(chars_idx) - source_idx  # Locate 1st idx of chars idx.
            while True:
                source = sources[source_idx]
                if chars[chars_idx: chars_idx + len(source)] == list(source):  # If source & its idx match chars list.
                    assembly.append(targets[source_idx])  # Put targets (replacements) into assembly.
                    chars_idx += len(source)  # Skip replaced indices of chars list.
                    break  # Break inner while once any replacement is done for a chars idx.

                if chars_idx not in indices[source_idx + 1:]:  # If no more indices aim at chars idx.
                    assembly.append(chars[chars_idx])
                    chars_idx += 1
                    break

                source_idx += indices[source_idx + 1:].index(chars_idx) + 1  # If other indices also aim at chars idx.
            continue

        assembly.append(chars[chars_idx])
        chars_idx += 1
