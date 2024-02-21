from trees.min_heap import MinHeap


def track_median(items_list):
    total_items = len(items_list)
    if total_items <= 0:
        return None

    medians_list = []

    min_heap = MinHeap([])  # Initialize min heap with an empty list.
    for i in range(total_items):
        min_heap.renew_items(numbers_list[:i + 1])
        medians_list.append(min_heap.find_median())

    return medians_list  # 10000


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    numbers_array_path = os.path.join(DATA_FOLDER_PATH, 'numbers_10000.txt')
    lines = open(numbers_array_path, 'r').readlines()
    numbers_list = [int(line.strip()) for line in lines]
    print(track_median(numbers_list))
