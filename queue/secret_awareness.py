
def count_secret_awareness(days: int, delay: int, forget: int):  # LeetCode Q.2327.
    current_day = 2  # Iteration starts at "day 2's beginning".
    delay_queue = [0] * (delay - 1)
    delay_queue.append(1)  # Already 1 person knows secret at day 2's start.
    memory_queue = [0] * (forget - delay)

    while True:
        memory_queue.pop(0)  # Step 1: some people forget secret at current day's beginning.

        memory_queue.append(delay_queue.pop(0))  # Step 2: move people who are off delay queue to memory queue.

        delay_queue.append(sum(memory_queue))  # Step 3: all people in memory queue can spread secret.

        current_day += 1
        if current_day > days:
            # Step 4: calculate awareness count. Prevent too big result.
            return (sum(memory_queue) + sum(delay_queue)) % (10 ** 9 + 7)
