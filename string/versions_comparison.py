
def compare_versions(version_1: str, version_2: str):
    version_1, version_2 = version_1.split('.'), version_2.split('.')
    version_1_len, version_2_len = len(version_1), len(version_2)

    if version_1_len > version_2_len:  # Pad up version 2 with 0.
        version_2.extend(['0'] * (version_1_len - version_2_len))

    if version_1_len < version_2_len:  # Pad up version 1 with 0.
        version_1.extend(['0'] * (version_2_len - version_1_len))
        version_1_len += version_2_len - version_1_len  # Update version 1's length as it will be used for iteration.

    for i in range(version_1_len):
        if int(version_1[i]) > int(version_2[i]):  # Version 1 wins.
            return 1
        if int(version_1[i]) < int(version_2[i]):  # Version 2 wins.
            return -1
    return 0  # Two versions tie.
