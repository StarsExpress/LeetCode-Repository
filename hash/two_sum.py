

def find_distinct_numbers(references: list | tuple | set):  # Return set of "distinct" integers and floats.
    if len(references) <= 0:
        return set()
    return set(filter(lambda x: isinstance(x, int) | isinstance(x, float), references))


def hash_references(references: list | tuple | set):  # Use hash table structure to seek all available two sums.
    if len(references) <= 1:  # Number of references is required to be at least two.
        return set()

    if isinstance(references, tuple) | isinstance(references, set):
        references = list(references)

    hash_set = set()  # Store all the "found sum" from two distinct numbers in references.
    for i in range(len(references) - 1):
        hash_set.update(set(map(lambda x: x + references[i], references[i + 1:])))
    return hash_set


def find_two_sum(targets: int | float | list | tuple | set, references: list | tuple | set):
    references = find_distinct_numbers(references)
    available_sums = hash_references(references)

    if isinstance(targets, int) | isinstance(targets, float):  # If target is int or float.
        if targets in available_sums:  # Target has distinct solutions in reference numbers.
            return 1
        return 0  # No distinct solutions in reference numbers.

    targets = find_distinct_numbers(targets)  # If target is either of list, tuple or set, ensure distinct numbers.
    return len(targets.intersection(available_sums))


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os
    import time

    start_time = time.time()
    numbers_array_path = os.path.join(DATA_FOLDER_PATH, 'int_1m.txt')
    lines = open(numbers_array_path, 'r').readlines()
    references_list = [int(line.strip()) for line in lines][:10000]
    print(len(hash_references(references_list)))
    # targets_list = [i for i in range(-10000, 10001)]
    # print(find_two_sum(targets_list, references_list))

    end_time = time.time()
    print(f'Total runtime: {str(round(end_time - start_time, 2))}.')
