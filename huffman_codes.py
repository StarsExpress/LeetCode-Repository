from config import DATA_FOLDER_PATH
import os
from trees.min_heap import MinHeap


def read_alphabets():
    alphabets_dict = dict()  # Skip the 1st line that isn't related to alphabet weight.
    alphabets = open(os.path.join(DATA_FOLDER_PATH, 'alphabets_1k.txt'), 'r').readlines()[1:]
    for alphabet in alphabets:
        weight = int(alphabet.replace('\n', ''))
        alphabets_dict.update({str(len(alphabets_dict) + 1): weight})  # Key: alphabet ordinal; value: weight.

    del alphabets, weight
    return alphabets_dict


def find_alphabet_given_min_weight(weight: int | float, alphabets_dict: dict):
    for alphabet in alphabets_dict.keys():
        if alphabets_dict[alphabet] == weight:
            return alphabet
    raise ValueError('Target weight not in dictionary.')


def merge_alphabets(alphabet_1: tuple | str, alphabet_2: tuple | str):
    if isinstance(alphabet_1, tuple):
        if isinstance(alphabet_2, tuple):
            return alphabet_1 + alphabet_2
        return alphabet_1 + (alphabet_2,)

    if isinstance(alphabet_2, tuple):
        return alphabet_2 + (alphabet_1,)
    return alphabet_1, alphabet_2


def find_coding_length(alphabets_dict: dict):
    if len(alphabets_dict) < 1:
        raise ValueError('Alphabets fewer than 1.')

    coding_len_dict = dict(zip(alphabets_dict.keys(), [0] * len(alphabets_dict)))  # Each alphabet's coding length.
    min_heap = MinHeap(list(alphabets_dict.values()))

    for _ in range(len(alphabets_dict) - 1):  # Given N alphabets, there will be N - 1 merges.
        min_weight_1 = min_heap.find_min(remove=True)
        min_alphabet_1 = find_alphabet_given_min_weight(min_weight_1, alphabets_dict)
        min_weight_2 = min_heap.find_min(remove=True)
        min_alphabet_2 = find_alphabet_given_min_weight(min_weight_2, alphabets_dict)

        min_heap.add_items(min_weight_1 + min_weight_2)  # Merge two min weights and update min heap & alphabets dict.
        del alphabets_dict[min_alphabet_1]  # Before merge, delete two alphabets from dict.
        del alphabets_dict[min_alphabet_2]
        alphabets_dict.update({merge_alphabets(min_alphabet_1, min_alphabet_2): min_weight_1 + min_weight_2})

        for min_alphabet in [min_alphabet_1, min_alphabet_2]:  # Update coding length.
            if isinstance(min_alphabet, tuple):
                for member in min_alphabet:
                    coding_len_dict[member] += 1
                continue
            coding_len_dict[min_alphabet] += 1

    assert len(alphabets_dict) == 1  # Should be merged into a single tree.
    assert len(set(list(alphabets_dict.keys())[0])) == len(coding_len_dict)  # All alphabets still exist.
    del alphabets_dict, min_alphabet_1, min_alphabet_2
    return min(coding_len_dict.values()), max(coding_len_dict.values())


if __name__ == '__main__':
    alphabets_dictionary = read_alphabets()
    min_coding_len, max_coding_len = find_coding_length(alphabets_dictionary)
    print(f'Min coding length: {min_coding_len}\nMax coding length: {max_coding_len}')
