
def compress_string(chars: list[str]):  # LeetCode Q.443: required to "modify" (not copies) chars list.
    if len(chars) <= 0:
        return 0

    if len(set(chars)) == 1:
        char, count = chars[0], len(chars)
        chars.clear()
        chars.append(char)
        if count > 1:
            for s in str(count):
                chars.append(s)
        return len(''.join(chars))

    start_idx, end_idx = 0, 1  # Iteration starts from 2nd char.
    streak = chars[start_idx: end_idx]
    past, present, future = [], [], []
    while True:
        if end_idx >= len(chars):
            present.append(chars[start_idx])
            if len(streak) > 1:
                for s in str(len(streak)):
                    present.append(s)

            past, future = chars[:start_idx], chars[end_idx:]
            chars.clear()
            chars.extend(past)
            chars.extend(present)
            chars.extend(future)
            return len(''.join(chars))

        if chars[end_idx] in streak:
            streak.append(chars[end_idx])
            end_idx += 1
            continue

        present.append(chars[start_idx])
        if len(streak) > 1:
            for s in str(len(streak)):
                present.append(s)

        past, future = chars[:start_idx], chars[end_idx:]
        chars.clear()
        chars.extend(past)
        chars.extend(present)
        chars.extend(future)

        start_idx += len(present)
        end_idx += start_idx + 1 - end_idx

        past.clear()
        present.clear()
        future.clear()

        streak.clear()
        streak.append(chars[start_idx])
