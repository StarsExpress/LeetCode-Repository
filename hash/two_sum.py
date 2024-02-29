from queue import Queue


def find_distinct_numbers(references: list | tuple | set):  # Return list of "distinct" integers and floats.
    if len(references) <= 0:
        return list()
    return list(filter(lambda x: isinstance(x, int) | isinstance(x, float), references))


def search_hash(target: int | float, references: list, hash_table: dict):
    for reference in references:
        diff = target - reference
        if diff in hash_table and reference != diff:
            return 1
    return 0


def find_two_sum(targets: int | float | list, references: list | tuple | set, queue_obj: Queue):
    references = find_distinct_numbers(references)
    if len(references) <= 0:
        queue_obj.put(0)
        return

    hash_table = dict()
    for reference in references:
        hash_table[reference] = True

    if isinstance(targets, int) or isinstance(targets, float):
        queue_obj.put(search_hash(targets, references, hash_table))
        return

    if len(targets) <= 0:
        queue_obj.put(0)
        return

    if len(targets) == 1:
        queue_obj.put(search_hash(targets[0], references, hash_table))
        return

    count, current_target = 0, targets[0]  # Current target starts from 1st item.
    while True:
        count += search_hash(current_target, references, hash_table)
        targets.remove(current_target)

        if -current_target in targets:
            count += search_hash(-current_target, references, hash_table)
            targets.remove(-current_target)

        if len(targets) <= 0:
            break
        current_target = targets[0]

    queue_obj.put(count)


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os
    import threading
    import time

    start_time = time.time()
    numbers_array_path = os.path.join(DATA_FOLDER_PATH, 'int_1m.txt')
    lines = open(numbers_array_path, 'r').readlines()
    references_list = [int(line.strip()) for line in lines]
    targets_list = [i for i in range(-10000, 10001)]

    queue_object = Queue()
    threading.stack_size(67108864)
    thread = threading.Thread(target=find_two_sum, args=(targets_list, references_list, queue_object))
    thread.start()
    thread.join()
    print(queue_object.get())

    end_time = time.time()
    print(f'Total runtime: {str(round(end_time - start_time, 2))}.')
