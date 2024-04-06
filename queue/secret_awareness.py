
def count_secret_awareness(days: int, delay: int, forget: int):  # LeetCode Q.2327.
    if min(days, delay, forget) < 1:
        raise ValueError('All 3 parameters must >= 1.')
    if not days >= forget > delay:
        raise ValueError('Relationship of days >= forget > delay must hold.')

    awareness, current_day = 1, 2  # Iteration starts at "day 2's beginning".
    delay_queue = [0] * (delay - 1)
    delay_queue.append(1)  # Already 1 person knows secret at day 2's start.
    memory_queue = [0] * (forget - delay)

    while True:
        awareness -= memory_queue.pop(0)  # Step 1: awareness drops as some people forget secret.

        memory_queue.append(delay_queue.pop(0))  # Step 2: move people who are off delay queue to memory queue.

        delay_queue.append(sum(memory_queue))  # Step 3: all people in memory queue can spread secret.

        awareness += sum(memory_queue) + sum(delay_queue) - awareness  # Step 4: update awareness count.

        current_day += 1
        if current_day > days:
            return awareness % (10 ** 9 + 7)  # Prevent too big result.
