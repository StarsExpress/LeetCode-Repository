from trees.min_heap import MinHeap
from trees.max_heap import MaxHeap


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    numbers_array_path = os.path.join(DATA_FOLDER_PATH, 'numbers_10000.txt')
    lines = open(numbers_array_path, 'r').readlines()
    numbers_list = [int(line.strip()) for line in lines]
    print(numbers_list)
    min_heap = MinHeap(numbers_list)
    assert min_heap.sort() == sorted(numbers_list)
    print(min_heap.sort())

    max_heap = MaxHeap(numbers_list)
    assert max_heap.sort() == sorted(numbers_list, reverse=True)
    print(max_heap.sort())
