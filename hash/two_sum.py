

def gather_distinct_numbers(references: list | tuple | set):  # Return distinct integers and floats.
    return set(filter(lambda x: isinstance(x, int) | isinstance(x, float), references))


def find_two_sum(target: int | float | list | tuple | set, references: list | tuple | set,
                 hash_table=None, return_hash=False):
    if hash_table is None:
        hash_table = dict()  # Hash table: keys and values are just int or float themselves.

    if isinstance(target, int) | isinstance(target, float):  # If target is int or float.
        for ref_number in references:
            if target - ref_number not in hash_table.keys():
                hash_table.update({ref_number: ref_number})
                continue  # Continue to next iteration of outer for loop.

            return ref_number, target - ref_number  # Target has distinct solutions in reference numbers.
        return None  # No distinct solutions in reference numbers.

    if len(target) == 1:  # If target is either of list, tuple or set and has only one item.
        if isinstance(target[0], int) | isinstance(target[0], float):  # Check if item is int or float.
            for ref_number in references:  # Iterate through all reference items.
                if target[0] - ref_number not in hash_table.keys():
                    hash_table.update({ref_number: ref_number})
                    continue  # Continue to next iteration of for loop.

                if return_hash:
                    return 1, hash_table  # Return 1 & hash table as target has distinct solutions in reference numbers.
                return 1

        if return_hash:
            return 0, hash_table  # Return 0 & hash table as target has no distinct solutions or isn't int nor float.
        return 0

    count = find_two_sum(target[:len(target) // 2], references, hash_table, True)[0]  # Count in 1st half.
    count += find_two_sum(target[len(target) // 2:], references, hash_table, True)[0]  # Count in 2nd half.

    if return_hash:
        return count, hash_table
    return count


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os
    import time

    start_time = time.time()
    numbers_array_path = os.path.join(DATA_FOLDER_PATH, 'int_1m.txt')
    lines = open(numbers_array_path, 'r').readlines()
    references_list = [int(line.strip()) for line in lines]
    references_list = gather_distinct_numbers(references_list)
    targets_list = [i for i in range(-10000, 10001)]
    print(find_two_sum(targets_list, references_list))

    end_time = time.time()
    print(f'Total runtime: {str(round(end_time - start_time, 2))}.')
